# Z3 Asset Index

A project to rebuild Z3's internal file structure, so that [Escartem](https://github.com/Escartem)'s [AnimeStudio](https://github.com/Escartem/AnimeStudio) can extract assets "byContainer".

Unlike a specific turn-based game, which has the internal containers kept within the blocks, meaning there's no real need for an Asset-Index, Z3 instead hashes the containers with xxhash64, which is what leads to AnimeStudio just dumping thousands of files into folders named by the typeID of the file (Texture2D/Mesh/Animator, etc).

I wanted to be able to find assets, especially Texture2D, more easily by having them sorted, which led me down this particular rabbit-hole. This method also allows correct extraction of duplicates, without getting swamped with 30 files that are all called the same thing and simply appended with (0), (1), (2).

## Generation

- Used AnimeStudio to generate a full asset_map of the game.
- Extracted all valid containerIDs from the asset_map.
- Extracted various lists of files based on typeID from the asset_map.
- Extracted all visible strings from ZenlessData /Data and /FileCFG.
- Scraped strings from MonoBehaviour files using my modified fork of AnimeStudio.
- Ran trillions of potential path/file combinations through a brute-forcing script.
- Ran the game with Frida hooking into certain RVAs that deal with hashing and texture loading.
- Created several Injector DLLs to try and scrape strings from memory and certain RVAs.

## Progress

Some reported numbers from the AssetMap might be a bit skewed, due to the inclusion of files like resources.assets and many duplicates.

- Note: Multiple Unity files like .prefab, .playable, .asset, and .unity can encompass multiple AnimeStudio asset types.

### By Type (Not Including Hidden)
| typeID                  | AssetMap Total | Remaining   | % Indexed | Update Diff |
| ----------------------- | -------------- | ------------| --------- |-------------|
| AnimationClip           | 28,170         | 8,315       | 70.49%    | +8.82%      |
| Animator                | 7,638          | 2,166       | 71.65%    | +15.70%     |
| Material                | 56,645         | 26,929      | 52.47%    | +5.52%      |
| Mesh                    | 72,720         | 33,420      | 54.05%    | +23.44%     |
| MonoBehaviour           | 299,455        | 83,277      | 72.20%    | +3.55%      |
| TextAsset               | 20,913         | 8,556       | 59.09%    | -10.48%     |
| Texture2D               | 62,647         | 14,513      | 76.84%    | +0.37%      |
| TOTAL                   | 548,188        | 177,176     | 67.68%    | +12.49%     |

### By Extension

Some reported numbers might be a bit skewed, due to HoYo consistency.

| Extension       | Amount      | Update Diff |
| --------------- | ----------- |-------------|
| .amr            | 2           | +2 (NEW)    |
| .anim           | 1,365       | +189        |
| .asset          | 178,230     | +128,237    |
| .bytes          | 10,990      | +1,538      |
| .compute        | 5           | +5 (NEW)    |
| .controller     | 72          | +72 (NEW)   |
| .cs             | 3           | +3 (NEW)    |
| .csv            | 1           | 0           |
| .exr            | 941         | +941 (NEW)  |
| .fbx            | 47,774      | +9,348      |
| .hdr            | 5           | +5 (NEW)    |
| .he             | 606         | +606 (NEW)  |
| .html           | 3           | 0           |
| .jpg            | 18          | +4          |
| .json           | 659         | +103        |
| .mask           | 3           | +3 (NEW)    |
| .mat            | 26,211      | +6,803      |
| .mesh           | 6,720       | +1,446      |
| .otf            | 7           | 0           |
| .physicMaterial | 2           | +2 (NEW)    |
| .playable       | 2,996       | +2,686      |
| .png            | 22,819      | +4,128      |
| .prefab         | 46,071      | +14,499     |
| .psd            | 1,452       | +162        |
| .shader         | 10          | +10 (NEW)   |
| .shadervariants | 394         | +217        |
| .unity          | 40          | +40 (NEW)   |
| .tga            | 21,426      | +2,678      |
| .tif            | 2           | +2 (NEW)    |
| .ttf            | 4           | +4 (NEW)    |
| .txt            | 776         | +391        |
| TOTAL           | 369,607     | +174,124    |

## Issues

As I only have a couple of usable RVAs to try and hook into, many files simply get read as .prefab files and paths, without showing where the actual files used are streamed from. Likewise, brute-forcing, as per its nature, is incredibly hit-or-miss;

I have been unable to find the paths for these files:

| Asset Type                                  | Amount |
| ------------------------------------------- | ------ |
| Story Comics                                | ~1,700 |
| Weapon Textures                             | ~300   |
| Various EFF/VX/Mask/HLOD textures/materials | 2000+  |
| Agent Mindscape Images                      | ~150   |
| All Live2D spines/atlases/skeletons         | A lot  |

## Thanks

* [Escartem](https://github.com/Escartem)
* [yarik0chka](https://github.com/yarik0chka)
* [Dimbreath](https://github.com/Dimbreath)
* [hrothgar234567](https://github.com/hrothgar234567)
* [undefined9071](https://github.com/undefined9071)
* Nullable
* [Razmoth](https://github.com/Razmoth)
