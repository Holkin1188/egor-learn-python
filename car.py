carName = input('Введите название автомобиля:');
carModel = input('введитена название модели:')
horsPower = int(input('Введите колличесто лошадей:'))
carWeight = int(input('введите массу автомобиля:'))
obem = int(input('введите обьем двигателя'))
obBaca = int(input('введите обьем бака'))


def getHorsOnWeight (weight, horse):
    resaul = weight / horse;
    return resaul

def getObemOnBaca (obbem, obbBaca):
    return obBaca / obbem

print('123')
userCar = {
    'car_name': carName,
    'car_model': carModel,
    'hors_power': horsPower,
    'car_weight': carWeight,
    'obem': obem,
    'obbem_baca': obBaca
}

