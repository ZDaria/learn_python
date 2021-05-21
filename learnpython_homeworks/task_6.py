import ephem


mars = ephem.Sun('2021/05/21')

const = ephem.constellation(mars)

print(const)

