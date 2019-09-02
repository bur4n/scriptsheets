# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
How to create a changelog? [Keepachangelog](https://keepachangelog.com/es-ES/1.0.0/)

## [Unreleased]
- Timestamp in log files.
- Allow to log the filter result.


## [0.4] - 2019-09-02
### Added
- Create the changelog.
- New argument (filter).
- Argument filter: group domains in the same IP.
- Delete duplicated domains in the list/arguments.
- New folder structure.

### Changed
- Delete row numbers in log file.

## [0.3] - 2019-08-30
### Added
- New argument (file).
- Argument file: allow load external file with a list of domains (one per line).

## [0.3] - 2019-08-30
### Added
- New argument (file).
- Argument file: allow load external file with a list of domains (one per line).

## [0.2] - 2019-08-29
### Added
- Add some new arguments (domains, log-error, verbose and version)
- Argument domains: you can set different domains separated by space.
- Argument log-error: store domains without IP in a different log file.
- Argument version: get script version.

## [0.1] - 2019-08-27
### Added
- First upload.
- Massive nslookup only from domains in a list.
- It stored the output in two files: massivenslookup_result.log and massivenslookup_error.log.