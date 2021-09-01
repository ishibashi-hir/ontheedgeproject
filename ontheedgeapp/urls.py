from django.urls import path
from .views import signupview, loginview , logoutview, headlineview, datalistview, setlistview, \
    resultcategorylistview, createresultcategoryview, updateresultcategoryview, deleteresultcategory, \
    taskcategorylistview, createtaskcategoryview, updatetaskcategoryview, deletetaskcategory, \
    itemlistview, createitemview, updateitemview, deleteitem, \
    gradelistview, creategradeview, updategradeview, deletegrade, \
    tasklistview, createtaskview, updatetaskview, deletetask, \
    inspectionlistview, updateinspectionview, deleteinspection, back2taskview,\
    failreportview, \
    picrecordlistview, updatepicrecordview, deletepicrecord 
    #createinspectionview, createpicrecordview, shotview, analyzeview,   
urlpatterns = [
    path('headline/', headlineview, name='headline'),
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
    path('datalist/', datalistview, name='datalist'),
    path('setlist/', setlistview, name='setlist'),

    #検査結果カテゴリー
    path('resultcategorylist/', resultcategorylistview, name='resultcategorylist'),
    path('createresultcategory/', createresultcategoryview, name='createresultcategory'),
    path('updateresultcategory/<int:pk>', updateresultcategoryview, name='updateresultcategory'),
    path('deleteresultcategory/<int:pk>', deleteresultcategory.as_view(), name='deleteresultcategory'),

    #タスクカテゴリー
    path('taskcategorylist/', taskcategorylistview, name='taskcategorylist'),
    path('createtaskcategory/', createtaskcategoryview, name='createtaskcategory'),
    path('updatetaskcategory/<int:pk>', updatetaskcategoryview, name='updatetaskcategory'),
    path('deletetaskcategory/<int:pk>', deletetaskcategory.as_view(), name='deletetaskcategory'),

    #商品
    path('itemlist/', itemlistview, name='itemlist'),
    path('createitem/', createitemview, name='createitem'),
    path('updateitem/<int:pk>', updateitemview, name='updateitem'),
    path('deleteitem/<int:pk>', deleteitem.as_view(), name='deleteitem'),

    #商品グレード
    path('gradelist/', gradelistview, name='gradelist'),
    path('creategrade/', creategradeview, name='creategrade'),
    path('updategrade/<int:pk>', updategradeview, name='updategrade'),
    path('deletegrade/<int:pk>', deletegrade.as_view(), name='deletegrade'),

    #タスク
    path('tasklist/', tasklistview, name='tasklist'),
    path('createtask/', createtaskview, name='createtask'),
    path('updatetask/<int:pk>', updatetaskview, name='updatetask'),
    path('deletetask/<int:pk>', deletetask.as_view(), name='deletetask'),

    #検査
    path('inspectionlist/', inspectionlistview, name='inspectionlist'),
    #path('createinspection/<int:pk>', createinspectionview, name='createinspection'),
    path('updateinspection/<int:pk>', updateinspectionview, name='updateinspection'),
    path('deleteinspection/<int:pk>', deleteinspection.as_view(), name='deleteinspection'),
    path('back2task/<int:pk>', back2taskview, name='back2task'),

    #画像記録
    path('picrecordlist/', picrecordlistview, name='picrecordlist'),
    #path('createpicrecord/<int:pk>', createpicrecordview, name='createpicrecord'),
    path('updatepicrecord/<int:pk>', updatepicrecordview, name='updatepicrecord'),
    path('deletepicrecord/<int:pk>', deletepicrecord.as_view(), name='deletepicrecord'),

    #path('analyze/<int:pk>', analyzeview, name='analyze'),
    path('failreport/', failreportview, name='failreport')

]
