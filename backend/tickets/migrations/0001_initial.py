# Generated by Django 3.0.2 on 2020-05-13 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workflows', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('name', models.CharField(blank=True, default='', max_length=112, verbose_name='标题')),
                ('sn', models.CharField(blank=True, help_text='工单的流水号', max_length=25, verbose_name='流水号')),
                ('participant', models.CharField(blank=True, default='', max_length=50, verbose_name='当前处理人')),
                ('customfield', models.TextField(default=[], verbose_name='所有表单数据')),
                ('create_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.State', verbose_name='当前状态')),
                ('transition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflows.Transition', verbose_name='进行状态')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.Workflow', verbose_name='工作流')),
            ],
            options={
                'verbose_name': '工单记录',
                'verbose_name_plural': '工单记录',
            },
        ),
        migrations.CreateModel(
            name='TicketUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('username', models.CharField(max_length=100, verbose_name='关系人')),
                ('in_process', models.BooleanField(default=False, verbose_name='待处理中')),
                ('worked', models.BooleanField(default=False, verbose_name='处理过')),
                ('ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tickets.Ticket')),
            ],
            options={
                'verbose_name': '工单关系人',
                'verbose_name_plural': '工单关系人',
            },
        ),
        migrations.CreateModel(
            name='TicketFlowLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('suggestion', models.CharField(blank=True, max_length=140, verbose_name='审批意见')),
                ('participant', models.CharField(blank=True, default='', max_length=50, verbose_name='处理人')),
                ('intervene_type', models.CharField(choices=[(0, '转交操作'), (1, '接单操作'), (2, '评论操作'), (3, '删除操作'), (4, '强制关闭操作'), (5, '强制修改状态操作'), (6, '撤回')], default=0, max_length=1, verbose_name='干预类型')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.State', verbose_name='当前状态')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket', verbose_name='工单')),
                ('transition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.Transition', verbose_name='流转')),
            ],
            options={
                'verbose_name': '工单流转日志',
                'verbose_name_plural': '工单流转日志',
            },
        ),
        migrations.CreateModel(
            name='TicketCustomField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('field_value', models.TextField(blank=True, default='', verbose_name='字段值')),
                ('customfield', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.CustomField', verbose_name='字段')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket', verbose_name='工单')),
            ],
            options={
                'verbose_name': '工单自定义字段值',
                'verbose_name_plural': '工单自定义字段值',
            },
        ),
    ]
