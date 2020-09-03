from django.db import models


class CaseDetail(models.Model):
    STAFF_ID = models.CharField(max_length=100, blank=False, default='')
    UNIT_CODE_DESC = models.CharField(max_length=100, blank=False, default='')
    APPL_ID = models.CharField(max_length=100, blank=False, default='')
    ID_NO = models.CharField(max_length=80, blank=False, default='')
    CUST_ID = models.CharField(max_length=80, blank=False, default='')
    CUST_NAME = models.CharField(max_length=200, blank=False, default='')
    GENDER = models.CharField(max_length=20, blank=False, default='')
    PRODUCT_GROUP = models.CharField(max_length=80, blank=False, default='')
    BUCKET_BOM = models.IntegerField()
    POS_BOM = models.IntegerField()
    LOAN_AMOUNT = models.FloatField()
    AMOUNT_OVERDUE = models.FloatField()
    INTEREST_OVERDUE = models.FloatField()
    PRINCIPLE_OUTSTANDING = models.FloatField()

    ACT_MOBILE = models.CharField(max_length=80, blank=False, default='')
    REMARKS = models.CharField(max_length=80, blank=False, default='')
    
    DOB = models.CharField(max_length=50, blank=False, default='')
    JOB_DESCRIPTION = models.CharField(max_length=200, blank=False, default='')
    FIRST_DUEDATE = models.CharField(max_length=50, blank=False, default='')
    RUNDATE = models.CharField(max_length=50, blank=False, default='')
    LAST_PAY = models.CharField(max_length=50, blank=False, default='')
    BIKE_TYPE = models.CharField(max_length=100, blank=False, default='')
    ACT_ADDRESS = models.CharField(max_length=300, blank=False, default='')
    REG_ADDRESS = models.CharField(max_length=300, blank=False, default='')
    GOOGLE_ADDRESS = models.CharField(max_length=300, blank=False, default='')
    LAT = models.FloatField()
    LON = models.FloatField()

    TYPE = models.CharField(max_length=100, blank=False, default='')
    CLASSIFY_CASE = models.CharField(max_length=100, blank=False, default='')
    RF_STATUS = models.CharField(max_length=100, blank=False, default='')
    DECILE_BUCKET = models.IntegerField()
    SCORE = models.IntegerField()

    BIN_VALUE_SCORE = models.CharField(max_length=100, blank=False, default='')
    BIN_VALUE = models.CharField(max_length=100, blank=False, default='')
    BIN_SORT = models.IntegerField()

    #--------- Dynamic ---------#
    # payment 
    TOTAL_PAY_AMOUNT = models.IntegerField()
    TODAY_PAID_AMT = models.IntegerField()
    TODAY_PAID = models.IntegerField()
    FULL_PAID = models.IntegerField()
    FOLLOWED = models.IntegerField()
    PTP_FLAG = models.IntegerField()
    LV1 = models.CharField(max_length=200, blank=False, default='')
    LV2 = models.CharField(max_length=200, blank=False, default='')
    LV3 = models.CharField(max_length=200, blank=False, default='')
    LV4 = models.CharField(max_length=200, blank=False, default='')
    LV5 = models.CharField(max_length=200, blank=False, default='')
    LV6 = models.CharField(max_length=200, blank=False, default='')

    TODO_FLAG = models.IntegerField()
    RECOMMEND = models.IntegerField()

    


class TotalView(models.Model):
    user = models.CharField(max_length=100, blank=False, default='')
    total_case = models.IntegerField()
