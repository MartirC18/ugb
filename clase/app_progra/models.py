from django.db import models
class VEHICULOS(models.Model):
    id_vehiculo=models.IntegerField
    marca=models.CharField(max_length=200)
    modelo=models.CharField(max_length=200)
    anio=models.IntegerField
    tipo=models.CharField(max_length=200)
    disponibilidad=models.CharField(max_length=200)

class CLIENTES(models.Model):
    id_cliente=models.IntegerField
    Nombre_Cliente=models.CharField(max_length=200)
    Apellido=models.CharField(max_length=200)
    Direccion=models.ForeignKey(Area,on_delete=models.CASCADE)
    Telefono=models.IntegerField
    Edad=models.IntegerField
    Sexo=models.CharField(max_length=200)

class EMPLEADOS(models.Model):
    id_empleado=models.IntegerField
    Nombre=models.CharField(max_length=200)
    Apellido=models.CharField(max_length=200)
    Edad=models.IntegerField
    Telefono=models.IntegerField
    Sexo=models.CharField(max_length=200)



class Registro(models.Model):
    cliente_id=models.CharField(max_length=200)
    vehiculo_id=models.IntegerField
    Fecha_Salida=models.DateField
    Fecha_Ingreso=models.DateField
    empleado_id=models.IntegerField
