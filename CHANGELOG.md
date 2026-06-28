# Changelog

## [2.2.1] - 2026-06-28

### Fixed
- reload coordinator on language change, fix OptionsFlow for HA 2024.11+ (v2.2.1)

### Other
- fix CHANGELOG.md

---

## [2.2.0] - 2026-06-27

### Added
- add bilingual support (EN/TH) selectable at install and via options (v2.2.0)

- Add CONF_LANGUAGE, LANG_EN, LANG_TH constants

- Config flow shows English / ภาษาไทย selector at install time

- OptionsFlow allows language change post-install via Configure button

- API returns both _en and _th fields for all text fields

- Sensors use coordinator.language to pick correct language field

- _last_text() fix for TMD API duplicate-element bug (first English field contains Thai)

- Translations updated with language field and options flow section

- Add CHANGELOG.md 

### Other
- add screenshot
