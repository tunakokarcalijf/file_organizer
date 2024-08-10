class Extensions:
    IMAGES: dict[str, list[str]] = {
        "COMMON": [
            ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".ico"
        ],
        "UNCOMMON": [
            ".tif", ".heic", ".heif", ".avif", ".raw", ".cr2", ".nef", ".orf", ".sr2", ".psd",
            ".ai", ".eps", ".jp2", ".j2k", ".jpf", ".jpx", ".jpm", ".dng", ".arw", ".rw2", ".raf",
            ".pef", ".3fr", ".srf", ".srw", ".x3f", ".bay", ".ciff", ".cs1", ".erf", ".fff",
            ".mef", ".mos", ".mrw", ".nrw", ".ptx", ".r3d", ".rwl", ".rwz", ".dcr", ".k25", ".kdc",
            ".dds", ".tga", ".icns"
        ]
    }

    AUDIOS: dict[str, list[str]] = {
        "COMMON": [
            ".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"
        ],
        "UNCOMMON": [
            ".alac", ".aiff", ".au", ".amr", ".opus", ".pcm", ".aif", ".aifc", ".mka", ".mid",
            ".midi", ".mpa", ".mogg"
        ]
    }

    VIDEOS: dict[str, list[str]] = {
        "COMMON": [
            ".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".mpg", ".mpeg"
        ],
        "UNCOMMON": [
            ".m4v", ".3gp", ".3g2", ".vob", ".ogv", ".mts", ".m2ts", ".ts", ".mxf", ".rm",
            ".rmvb", ".asf", ".divx", ".f4v", ".svi"
        ]
    }

    DOCUMENTS: dict[str, list[str]] = {
        "TEXT": [
            ".txt", ".md", ".rtf", ".doc", ".docx", ".odt", ".tex", ".wps"
        ],
        "DATA": [
            ".csv", ".tsv", ".json", ".xml", ".yaml", ".yml", ".sqlite", ".db", ".sql", ".parquet",
            ".h5", ".dta", ".sav", ".rda", ".xls", ".xlsx", ".ods"
        ],
        "PRESENTATION": [
            ".ppt", ".pptx", ".key", ".odp", ".pps", ".ppsx"
        ],
        "EBOOK": [
            ".epub", ".mobi", ".azw"
        ],
        "OTHER": [
            ".xps", ".chm"
        ]
    }

    SCRIPTS: dict[str, list[str]] = {
        "PYTHON": [
            ".py", ".pyw", ".pyx", ".pyd", ".pyi"
        ],
        "JUPYTER_NOTEBOOK": [
            ".ipynb"
        ],
        "HTML": [
            ".html", ".htm", ".xhtml"
        ],
        "CSS": [
            ".css"
        ],
        "JAVASCRIPT": [
            ".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx"
        ],
        "PHP": [
            ".php", ".php3", ".php4", ".php5", ".phtml", ".phpt"
        ],
        "SQL": [
            ".sql"
        ]
    }

    ARCHIVES: dict[str, list[str]] = {
        "COMMON_ARCHIVES": [
            ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".lz", ".z", ".arj", ".cab",
            ".iso", ".tar.gz", ".tar.bz2", ".tar.xz", ".tgz", ".tbz2", ".txz", ".taz", ".lzma",
            ".lz4", ".zstd", ".cpio", ".rpm", ".deb"
        ],
        "MAC_ARCHIVES": [
            ".dmg", ".pkg"
        ],
        "JAVA_ARCHIVES": [
            ".jar", ".war", ".ear"
        ]
    }

    CONFIGURATIONS: list[str] = [
        ".conf", ".cfg", ".ini", ".yml", ".yaml", ".properties", ".env"
    ]

    LOG_FILES: list[str] = [
        ".log", ".out", ".err", ".trace", ".dump"
    ]

    DATABASES: list[str] = [
        ".db", ".sqlite", ".dmp", ".mdb", ".accdb", ".cdb", ".ndf", ".log"
    ]

    SYSTEM_FILES: list[str] = [
        ".sys", ".dll", ".drv", ".bat", ".sh", ".cmd", ".msi", ".iso"
    ]

    FONTS: list[str] = [
        ".ttf", ".otf", ".woff", ".woff2", ".eot", ".bdf", ".pfb", ".afm"
    ]
