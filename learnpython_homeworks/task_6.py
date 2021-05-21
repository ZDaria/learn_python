import ephem

mars = ephem.Moon('2021/05/22')
const = ephem.constellation(mars)

print(const)

