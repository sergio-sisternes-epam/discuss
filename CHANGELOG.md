# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Updated the direct Atlas dependency from `v0.8.13` to `v0.8.14`.

## [0.3.7] - 2026-09-04

### Added

- Added the Discuss skill for durable, agent-maintained discussion graphs,
  including speak, sprout, termination, lint, consolidation, and constellation
  paths.
- Added KVA graph rules, adversarial scenarios, and repository-owned linting.
- Added reproducible APM dependency locking, source and consumer CI, and
  exact-main release-readiness automation.

### Changed

- Migrated the discussion store from the deprecated custom mount to
  `.atlas/github.com/sergio-sisternes-epam/discuss-atlas`.
- Pinned Atlas to `v0.8.13`; Atlas owns the transitive OKF dependency.
- Updated consumer guidance to mount and resolve the private discussion store
  separately from APM package installation.

### Fixed

- Required the human-facing speak path and `speak_loaded` activation receipt.
- Clarified that the discussion store git root is the OKF root.

[Unreleased]: https://github.com/sergio-sisternes-epam/discuss/compare/v0.3.7...HEAD
[0.3.7]: https://github.com/sergio-sisternes-epam/discuss/releases/tag/v0.3.7
