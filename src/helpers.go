// Package helpers provides utility functions used throughout the project.
package helpers

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

// GetFilePath returns the absolute path of the file.
func GetFilePath(file string) string {
	return filepath.Abs(file)
}

// GetRootDir returns the root directory of the project.
func GetRootDir() string {
	wd, err := os.Getwd()
	if err != nil {
		panic(err)
	}
	return filepath.Abs(wd)
}

// GetRelativePath returns the relative path from the provided base path to the target file.
func GetRelativePath(basePath string, target string) string {
	base, _ := filepath.Abs(basePath)
	target, _ := filepath.Abs(target)
	return filepath.Rel(base, target)
}

// IsRelative checks if the provided path is relative.
func IsRelative(path string) bool {
	return !filepath.IsAbs(path)
}

// RemoveLeadingSlash removes the leading slash from the provided path.
func RemoveLeadingSlash(path string) string {
	if strings.HasPrefix(path, "/") {
		return strings.TrimPrefix(path, "/")
	}
	return path
}