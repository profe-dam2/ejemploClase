from math import asin

xGyroValue = float(splitdata[1] ) /100 *3.142 /180
yGyroValue = float(splitdata[2] ) /100 *3.142 /180
zGyroValue = float(splitdata[3] ) /100 *3.142 /180
xAxisValue = float(splitdata[4] ) /100
yAxisValue = float(splitdata[5] ) /100
zAxisValue = float(splitdata[6] ) /100

print(xGyroValue)
print(yGyroValue)
print(zGyroValue)
print(xAxisValue)
print(yAxisValue)
print(zAxisValue)


zGyroAngleValue = zGyroAngleValue + zGyroValue *0.05


xAxisAngleValue = asin(yAxisValue /zAxisValue)
yAxisAngleValue = asin(xAxisValue /zAxisValue)

xAngleValue = 0.98 * (xAngleValue + xGyroValue *0.05 ) +0.02 *xAxisAngleValue
yAngleValue = 0.98 * (yAngleValue - yGyroValue *0.05 ) +0.02 *yAxisAngleValue

print(xAngleValue)
print(yAngleValue)
print(zGyroAngleValue)


# rotateX(xAngleValue)
# rotateY(zGyroAngleValue)
# rotateZ(yAngleValue)