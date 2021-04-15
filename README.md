# DirFlattener
A Python script for flattening a directory tree

* Files are flattened to the first child directory. 
* In case of filename collisions, the file is renamed using the path

**THIS SCRIPT MOVES FILES AND DELETES DIRECTORIES! USE WITH CAUTION!**

#  Usage
```
$ python3 dirflatten.py <directory>
```

# Example
## Before
```
$ tree photos/
photos/
├── 2015
│   ├── Aug
│   │   ├── IMG73.jpg
│   │   └── IMG81.jpg
│   ├── Jan
│   │   ├── IMG73.jpg
│   │   ├── IMG87.jpg
│   │   └── IMG99.jpg
│   └── Jul
│       ├── IMG55.jpg
│       └── IMG56.jpg
├── 2016
│   ├── Feb
│   │   ├── IMG97.jpg
│   │   └── IMG99.jpg
│   └── May
│       ├── IMG21.jpg
│       ├── IMG22.jpg
│       └── IMG23.jpg
└── 2017
    └── Nov
        └── IMG94.jpg

9 directories, 13 files
```

## After
```
$ python3 dirflatten.py photos
$ tree mydir/
photos/
├── 2015
│   ├── IMG55.jpg
│   ├── IMG56.jpg
│   ├── IMG73.jpg
│   ├── IMG81.jpg
│   ├── IMG87.jpg
│   ├── IMG99.jpg
│   └── photos_2015_Aug_IMG73.jpg
├── 2016
│   ├── IMG21.jpg
│   ├── IMG22.jpg
│   ├── IMG23.jpg
│   ├── IMG97.jpg
│   └── IMG99.jpg
└── 2017
    └── IMG94.jpg

3 directories, 13 files
```

