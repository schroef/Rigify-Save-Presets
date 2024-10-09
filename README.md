# Rigify Save Presets

This addon makes it possible to save rig setup to a preset folder. The function was already existing but would generate a text inside Blender. I simply added some new functions so these presets can directly be saved in the Blender preset folder of Metarigs. Presets can be added to a folder as well as new folders can be created.

The added presets can then be loaded directly using the add menu. To get the new preset to show, you need to either restart blender or reload the all the addons pressing F8. Its also now possible save Rigify main settings as presets. These can be loaded at any time, no need for a refresh.

>NB with the new implementation of Bone Collections. When applying a preset, i can happen that bones are not placed in a bone collection. Ive added an operator which checks for existing collection and show dialog what is missing 

!['Example Rig Presets'](https://raw.githubusercontent.com/wiki/schroef/Rigify-Save-Presets/images/rigify-save-presets-v012.png?v20241009)


## Rigify Addon

Rigify helps automate the creation of character rigs. It is based around a building-blocks approach, where you build complete rigs out of smaller rig parts (e.g. arms, legs, spines, fingers...). The rig parts are currently few in number, but as more rig parts are added to Rigify it should become more and more capable of rigging a large variety of characters and creatures.

Rigify also operates on the principle that once a rig is created, that rig should no longer need Rigify. This means you can always distribute rigs created with Rigify to people who do not have it and the rigs will still function completely.

It is important to note that Rigify only automates the creation of the rig controls and bones. It does not attach the rig to a mesh, so you still have to do skinning etc. yourself.

!['Example Rigify Metarig'](https://raw.githubusercontent.com/wiki/schroef/Rigify-Save-Presets/images/Addon_Rigify_0.5_split_metarig.png?v20241007)

>Addon documentation can be found at: <b>[Rigify manual](https://docs.blender.org/manual/en/latest/addons/rigging/rigify/index.html)</b>


### System Requirements

| **OS** | **Blender** |
| ------------- | ------------- |
| OSX | Not Tested |
| Windows | Blender 4.0+ |
| Linux | Not Tested |


### Installation Process

1. Download the latest <b>[release](https://github.com/schroef/rigify-save-presets/releases/)</b>
2. If you downloaded the zip file.
3. Open Blender.
4. Go to File -> User Preferences -> Addons.
5. At the bottom of the window, choose *Install From File*.
6. Select the file `rigify-master.zip` from your download location..
7. Activate the checkbox for the plugin that you will now find in the list.

>this addon requires <b>Rigify</b> to be active<br>
>Older 2.80 - 3.6.0 version can be found in this branch: <b>[Rigify-Save-Presets bl2.80-bl3.60](https://github.com/schroef/Rigify-Save-Presets/tree/bl-280)</b><br>
>Older 2.79 version can be found in this branch: <b>[Rigify-Save-Presets bl2.79](https://github.com/schroef/Rigify-Save-Presets/tree/bl-279)</b><br>


### Changelog
[Full Changelog](CHANGELOG.md)

<!--
- Fill in data
 -
 -
-->

