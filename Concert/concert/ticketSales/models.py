from django.db import models
from jalali_date import date2jalali,datetime2jalali
from accounts.models import ProfileModel

# Create your models here.


class concertModel (models.Model):
    
    class Meta:
        verbose_name="کنسرت"
        verbose_name_plural="کنسرت"

    Name=models.CharField(max_length=100,verbose_name="نام کنسرت")
    SingerName=models.CharField(max_length=100 ,verbose_name="خواننده")
    lenght=models.IntegerField(verbose_name="مدت زمان")
    Poster=models.ImageField(upload_to="concertImages/",null=True,verbose_name="پوستر")

    def __str__(self):
        return self.SingerName


class locationModel(models.Model):
    class Meta:
        verbose_name="محل برگزاری"
        verbose_name_plural="محل برگزاری"

    IdNumber=models.IntegerField(primary_key=True,verbose_name="کد محل")
    Name=models.CharField(max_length=100,verbose_name="نام محل")
    Address=models.CharField(max_length=500,default="تهران-برج میلاد",verbose_name="آدرس")
    Phone=models.CharField(max_length=11,null=True,verbose_name="تلفن")
    capacity=models.IntegerField(verbose_name="ظرفیت")

    def __str__(self):
        return self.Name
        

class timeModel(models.Model):
    class Meta:
        verbose_name="سانس"
        verbose_name_plural="سانس"

    concertModel= models.ForeignKey(to=concertModel,on_delete=models.PROTECT,verbose_name="کنسرت")
    locationModel = models.ForeignKey(to=locationModel,on_delete=models.PROTECT,verbose_name="محل برگزاری")
    StartDateTime=models.DateTimeField(verbose_name="تاریخ برگزاری")
    Seats=models.IntegerField(verbose_name="تعداد صندلی")

    Start=1
    End=2
    Cancle=3
    Sales=4
    status_chioces=((Start,"فروش بلیط شروع شده است"),
                    (End,"فروش بلیط تمام شده است"),
                    (Cancle,"این سانی کنسل شده است"),
                    (Sales,"در حال فروش بلیط"))

    Status=models.IntegerField(choices=status_chioces,verbose_name="وضعیت")

    def __str__(self):
        return "Time: {} ConcertName: {} Location: {}".format(self.StartDateTime,self.concertModel.Name,self.locationModel.Name)

    def get_jalai_date(self):
        return datetime2jalali(self.StartDateTime)


class ticketModel(models.Model):
    class Meta:
        verbose_name="بلیط"
        verbose_name_plural="بلیط"

    ProfileModel=models.ForeignKey(ProfileModel,on_delete=models.PROTECT,verbose_name="کاربر")
    timeModel=models.ForeignKey("timeModel",on_delete=models.PROTECT,verbose_name="سانس")
    ticketImage=models.ImageField(upload_to="TicketImages/",verbose_name="عکس")
    Name=models.CharField(max_length=100,verbose_name="عنوان")
    Price=models.IntegerField(verbose_name="مبلغ")

    def __str__(self):
        return "TicketInfo: Profile: {} ConcertInfo : {}".format(timeModel.__str__())