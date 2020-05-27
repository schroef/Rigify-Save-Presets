# Rigify Save Presets

This addon makes it possible to save rig setup to a preset folder. The function was already existing but would generate a text inside Blender. I simply added some new functions so these presets can directly be saved in the Blender preset folder of Metarigs. Presets can be added to a folder as well as new folders can be created.

The added presets can then be loaded directly using the add menu. To get the new preset to show, you need to either restart blender or reload the all the addons pressing F8. Its also now possible save Rigify main settings as presets. These can be loaded at any time, no need for a refresh.

!['Example Rig Presets'](https://raw.githubusercontent.com/wiki/schroef/rigify/images/rigify-save-presets-v007.png?v27-05-2020)


## Rigify Addon

Rigify helps automate the creation of character rigs. It is based around a building-blocks approach, where you build complete rigs out of smaller rig parts (e.g. arms, legs, spines, fingers...). The rig parts are currently few in number, but as more rig parts are added to Rigify it should become more and more capable of rigging a large variety of characters and creatures.

Rigify also operates on the principle that once a rig is created, that rig should no longer need Rigify. This means you can always distribute rigs created with Rigify to people who do not have it and the rigs will still function completely.

It is important to note that Rigify only automates the creation of the rig controls and bones. It does not attach the rig to a mesh, so you still have to do skinning etc. yourself.

!['Example Rigify Metarig'](https://en.blender.org/uploads/thumb/6/6b/Addon_Rigify_0.5_split_metarig.png/640px-Addon_Rigify_0.5_split_metarig.png)

>Addon documentation can be found at: <b>[Rigify Addon Extention page](https://en.blender.org/index.php/Extensions:2.6/Py/Scripts/Rigging/Rigify)</b>


### System Requirements

| **OS** | **Blender** |
| ------------- | ------------- |
| OSX | Blender 2.80+ |
| Windows | Not Tested |
| Linux | Not Tested |


### Installation Process

1. Download the latest <b>[release](https://github.com/schroef/rigify-save-presets/releases/)</b>
2. If you downloaded the zip file.
3. Open Blender.
4. Go to File -> User Preferences -> Addons.
5. At the bottom of the window, choose *Install From File*.
6. Select the file `rigify-master.zip` from your download location..
7. Activate the checkbox for the plugin that you will now find in the list.

>this addon requires <b>Rigify</b> to be active <br>
>Older 2.79 version can be found in this branch: <b>[Rigify-Save-Presets bl2.79](https://github.com/schroef/Rigify-Save-Presets/tree/bl-279)</b>


### Changelog
[Full Changelog](CHANGELOG.md)

<!--
- Fill in data
 -
 -
-->

