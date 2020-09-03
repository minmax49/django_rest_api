
## ĐÔi điều lưu ý

Django rest framework support tốt cho CSDL quan hệ 

Tuy nhiên NoSQL thì có vẻ không tiện bằng flask


khi start 1 app : vd worklist 

trong models.py khai báo như sau : 

```python
class TotalView(models.Model):
    user = models.CharField(max_length=100, blank=False, default='')
    total_case = models.IntegerField()
```



lúc này ngầm hiều rằng sẽ tạo ra collection: "worklist_totalview" <br>
nếu k muốn migrate thì tạo trước các collection cùng tên.
