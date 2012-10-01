formato = "%r %r %r %r"

print formato % (1,2,3,4)
print formato % ("um",'dois','tres','quatro')
print formato % (formato,formato,formato,formato)
print formato % (
      "eu fiz isso",
      'e esse tipo pode funcionar',
      'mas eu nao sei',
      'entao bom dia'
)
