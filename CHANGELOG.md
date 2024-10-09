# Changelog
All notable changes to this project will be documented in this file.

## [0.1.2] - 2024-10-09
### Fix
- When applying a Rig preset, we loose all bone collection placement. Due to new mechnism when removing all bone collection, prior set bones would loose the info
  Now when a Rig preset is applied, it check if names are the same. It can still happen that bones will not be placed into a collection. If so, a dialog will show which bones have no bone colelction and they will be all selected.

## [0.1.1] - 2024-10-08
### Fix
- Make it work in bl4.0+
  Update to bone collections

## [0.0.9] - 2020-11-30
### Fix
- Save custom folder button > label missed text=""

## [0.0.8] - 2020-06-03
### Fix
- Rig layers set selection code


## [0.0.7] - 2020-05-27
### Changed
- Update panel layout, bigger add preset button
- Added releases

## [0.0.6] - 2018-09-22
### Changed
- Update panel layout, bigger add preset button
- Added releases

## [0.0.5] - 2018-09-22
### Changed
- Cleaned code
- Delete old class

## [0.0.4] - 2018-09-22
### Changed
- Cleaned code
- Deleted old functions and classes

## [0.0.3] - 2018-09-22
### Added
- Option to save rigify settings presets, load/save preset settings for rigify while working on the meta rig.
- Changelog formating.

### Changed
- UI updated, same as advanced settings.

## [0.0.2] - 2018-09-21
### Changed
- Separated this function into its own addon for easier install using current installed version. It shows cleaner with no errors in the preferences tab.

## [0.0.1] - 2018-09-21
### Changed
- Easier method for save rig presets to the addon, initially done in main addon.

## Notes
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
<!--### Official Rigify Info-->

[0.1.1]:https://github.com/schroef/Rigify-Save-Presets/releases/tag/v0.1.1
[0.1.0]:https://github.com/schroef/Rigify-Save-Presets/releases/tag/v0.1.0
[0.0.9]:https://github.com/schroef/Rigify-Save-Presets/releases/tag/v0.0.9
[0.0.8]:https://github.com/schroef/Rigify-Save-Presets/releases/tag/v0.0.8
[0.0.7]:https://github.com/schroef/Rigify-Save-Presets/releases/tag/v0.0.7
[0.0.6]:https://github.com/schroef/Rigify-Save-Presets/releases/tag/v0.0.6
[0.0.5]:https://github.com/schroef/Rigify-Save-Presets/releases/tag/v0.0.5
[0.0.4]:https://github.com/schroef/Rigify-Save-Presets/releases/tag/v0.0.4
[0.0.3]:https://github.com/schroef/Rigify-Save-Presets/releases/tag/v0.0.3
[0.0.2]:https://github.com/schroef/Rigify-Save-Presets/releases/tag/v0.0.2
[0.0.1]:https://github.com/schroef/Rigify-Save-Presets/releases/tag/v0.0.1