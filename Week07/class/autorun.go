// Kraken
// Copyright (C) 2016-2020  Claudio Guarnieri
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <https://www.gnu.org/licenses/>.

package main

import (
	"os"
	"path/filepath"
	"time"

	log "github.com/Sirupsen/logrus"
	"github.com/botherder/go-autoruns/v2"
	"github.com/botherder/go-savetime/files"
)

func autorunDetected(autorun *autoruns.Autorun, signature string) *Detection {
	log.WithFields(log.Fields{
		"type":       autorun.Type,
		"image_path": autorun.ImagePath,
	}).Warning("DETECTION! Malicious autorun detected as ", signature)

	detection := NewDetection("autorun", autorun.ImagePath, autorun.ImageName, signature, 0)
	detection.ReportAndStore()

	return detection
}

func autorunStoreInDatabase(autorun *autoruns.Autorun, wasReported bool) {
	// Check if we have already seen this autorun before.
	db := NewDatabase()
	err := db.Open()
	if err != nil {
		log.Error("Failed to store autorun record in local database: ", err.Error())
		return
	}
	defer db.Close()

	isStored, _ := db.IsAutorunStored(autorun)
	if isStored == false {
		// If not, we store it in the local database with the appropriate marking.
		db.StoreAutorun(autorun, wasReported)

		log.WithFields(log.Fields{
			"path":      autorun.ImagePath,
			"arguments": autorun.Arguments,
		}).Debug("New autorun identified and stored in local database!")
	}
}

func autorunScan(autorun *autoruns.Autorun) *Detection {
	// We want to report autorun records even if they were not detected as malicous.
	wasReported := false
	if *report == true {
		err := apiAutorun(autorun)
		if err != nil {
			log.Error("Failed to report autorun record: ", err.Error())
		} else {
			log.Debug("Autorun record reported to server!")
			wasReported = true
		}
	}

	// We store data only if we run in daemon mode.
	if *daemon == true {
		// Store autorun in database if necessary.
		autorunStoreInDatabase(autorun, wasReported)

		// We backup the autorun file.
		if _, err := os.Stat(autorun.ImagePath); err == nil {
			dstPath := filepath.Join(StorageFiles, autorun.SHA1)
			if _, err := os.Stat(dstPath); os.IsNotExist(err) {
				files.Copy(autorun.ImagePath, dstPath)
			}
		}
	}

	// Lastly, we scan it.
	if _, err := os.Stat(autorun.ImagePath); err == nil {
		log.Debug("Scanning ", autorun.Type, " autorun at path ", autorun.ImagePath)
		matches, _ := scanner.ScanFile(autorun.ImagePath)
		for _, match := range matches {
			return autorunDetected(autorun, match.Rule)
		}
	}

	return nil
}

func autorunWatch() {
	log.Info("Starting autoruns monitor...")

	ticker := time.NewTicker(time.Minute * 30).C

	for {
		select {
		case <-ticker:
			for _, autorun := range autoruns.GetAllAutoruns() {
				autorunScan(autorun)
			}
		}
	}
}
