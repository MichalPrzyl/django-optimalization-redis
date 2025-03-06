from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=255)
    column_a = models.CharField(max_length=255, null=True)
    column_b = models.CharField(max_length=255, null=True)
    column_c = models.CharField(max_length=255, null=True)
    column_d = models.CharField(max_length=255, null=True)
    column_e = models.CharField(max_length=255, null=True)

class ProfileB(models.Model):
    name = models.CharField(max_length=255)
    column_a = models.CharField(max_length=255, null=True)
    column_b = models.CharField(max_length=255, null=True)
    column_c = models.CharField(max_length=255, null=True)
    column_d = models.CharField(max_length=255, null=True)
    column_e = models.CharField(max_length=255, null=True)

class ProfileC(models.Model):
    name = models.CharField(max_length=255)
    column_a = models.CharField(max_length=255, null=True)
    column_b = models.CharField(max_length=255, null=True)
    column_c = models.CharField(max_length=255, null=True)
    column_d = models.CharField(max_length=255, null=True)
    column_e = models.CharField(max_length=255, null=True)


class Person(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    profile = models.ForeignKey(Profile, models.CASCADE, null=True)
    profile_b = models.ForeignKey(ProfileB, models.CASCADE, null=True)
    profile_c = models.ForeignKey(ProfileC, models.CASCADE, null=True)


    column_a = models.CharField(max_length=255, null=True)
    column_b = models.CharField(max_length=255, null=True)
    column_c = models.CharField(max_length=255, null=True)
    column_d = models.CharField(max_length=255, null=True)
    column_e = models.CharField(max_length=255, null=True)
    column_f = models.CharField(max_length=255, null=True)
    column_g = models.CharField(max_length=255, null=True)
    column_h = models.CharField(max_length=255, null=True)
    column_i = models.CharField(max_length=255, null=True)
    column_j = models.CharField(max_length=255, null=True)
    column_k = models.CharField(max_length=255, null=True)
    column_l = models.CharField(max_length=255, null=True)
    column_m = models.CharField(max_length=255, null=True)
    column_n = models.CharField(max_length=255, null=True)
    column_o = models.CharField(max_length=255, null=True)
    column_p = models.CharField(max_length=255, null=True)
    column_r = models.CharField(max_length=255, null=True)
    column_s = models.CharField(max_length=255, null=True)
    column_t = models.CharField(max_length=255, null=True)
    column_u = models.CharField(max_length=255, null=True)
    column_w = models.CharField(max_length=255, null=True)
    column_x = models.CharField(max_length=255, null=True)
    column_y = models.CharField(max_length=255, null=True)
    column_z = models.CharField(max_length=255, null=True)
    column_e = models.CharField(max_length=255, null=True)
