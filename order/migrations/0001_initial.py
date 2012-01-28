# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ccOrder'
        db.create_table('order_ccorder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.IntegerField')()),
            ('product', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('format', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('time', self.gf('django.db.models.fields.IntegerField')()),
            ('circulation', self.gf('django.db.models.fields.IntegerField')()),
            ('paper', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('chromacity', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('file1', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('file2', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('cost', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('not_cash', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('need_deliver', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_delivered', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order_status', self.gf('django.db.models.fields.IntegerField')()),
            ('enter_date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('paramstr', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('order', ['ccOrder'])


    def backwards(self, orm):
        
        # Deleting model 'ccOrder'
        db.delete_table('order_ccorder')


    models = {
        'order.ccorder': {
            'Meta': {'object_name': 'ccOrder'},
            'chromacity': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'circulation': ('django.db.models.fields.IntegerField', [], {}),
            'client': ('django.db.models.fields.IntegerField', [], {}),
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'enter_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'file1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'file2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_delivered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_deliver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'not_cash': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order_status': ('django.db.models.fields.IntegerField', [], {}),
            'paper': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'paramstr': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['order']
