from tecombine import CombineArchive, KnownFormats

archive = CombineArchive()

# Add SBML
archive.addFile(
    './model/BIOMD0000000144.xml', # source path
    './model/BIOMD0000000144.xml', # dest path
    KnownFormats.lookupFormat('sbml'),
    False # master attribute
)

# Add SED-ML
archive.addFile(
    './experiment/Calzone2007-simulation-figure-1B.xml', # source path
    './experiment/Calzone2007-simulation-figure-1B.xml', # dest path
    KnownFormats.lookupFormat('sedml'),
    True # master attribute
)

archive.writeToFile('out.omex');
