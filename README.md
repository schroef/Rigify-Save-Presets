# Rigify Save Presets

This fork has a new section added which makes it possible to save rig setup to a preset folder. The function was already excisting but would generate a text inside blender. I simple added some new functions so these presets can directly be save in the blender preset folder of metarigs. Presets can be added to folder as well as new folders can be created.

These added preset can than be loaded directly using the add menu. To get the new preset to show, you need to either restart blender or reload the all the addons pressing F8

!['Example Rig Presets'](https://raw.githubusercontent.com/wiki/schroef/rigify/images/rigify-save-presets.png)


## Rigify Addon

Rigify helps automate the creation of character rigs. It is based around a building-blocks approach, where you build complete rigs out of smaller rig parts (e.g. arms, legs, spines, fingers...). The rig parts are currently few in number, but as more rig parts are added to Rigify it should become more and more capable of rigging a large variety of characters and creatures.

Rigify also operates on the principle that once a rig is created, that rig should no longer need Rigify. This means you can always distribute rigs created with Rigify to people who do not have it and the rigs will still function completely.

It is important to note that Rigify only automates the creation of the rig controls and bones. It does not attach the rig to a mesh, so you still have to do skinning etc. yourself.

!['Example Rigify Metarig'](https://en.blender.org/uploads/thumb/6/6b/Addon_Rigify_0.5_split_metarig.png/640px-Addon_Rigify_0.5_split_metarig.png)

>Addon documentation can be found at: <b>[Rigify Addon Extention page](https://en.blender.org/index.php/Extensions:2.6/Py/Scripts/Rigging/Rigify)</b>


### System Requirements

| **OS** | **Blender** |
| ------------- | ------------- |
| OSX | Blender 2.78+ |
| Windows | Not Tested |
| Linux | Not Tested |


### Installation Process

1. Download the zip <!--or fork to local system  <b>[fork release](https://github.com/schroef/TheaForBlender/releases/)</b>-->
2. If you downloaded the zip file.
3. Open Blender.
4. Go to File -> User Preferences -> Addons.
5. At the bottom of the window, choose *Install From File*.
6. Select the file `rigify-master.zip` from your download location..
7. Activate the checkbox for the plugin that you will now find in the list.

>this addon requires <b>Rigify</b> to be active


### Changelog
<!--[Full Changelog](https://github.com/skywinder/github-changelog-generator/compare/v1.15.0.pre.beta...v1.15.0-rc)-->

## [0.0.3] - 2018-09-22
### Added
- Option to save rigify settings presets, load/save preset settings for rigify while working on the meta rig
- Changelog formating
###

### Changed
- UI updated, same as advanced settings

## [0.0.2] - 2018-09-21
### Changed
- Separated this function into its own addon for easier install using current installed version. It shows cleaner with no errors in the preferences tab
###

## [0.0.1] - 2018-09-21
### Changed
- Easier method for save rig presets to the addon, initially done in main addon
###

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
<!--### Official Rigify Info-->




<!--
- Fill in data
 -
 -
-->

