import tellurium as te

# works
# inline_omex = te.convertCombineArchive('out_sedml.omex')
# doesn't work
inline_omex = te.convertCombineArchive('out_phrasedml.omex')
print('inline omex:')
print(inline_omex)
te.exportInlineOmex(inline_omex, 'out_tellurium.omex')
