# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'ccOrder.file_1c'
        db.add_column('order_ccorder', 'file_1c', self.gf('django.db.models.fields.files.FileField')(default=1, max_length=100, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'ccOrder.file_1c'
        db.delete_column('order_ccorder', 'file_1c')


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
            'file_1c': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_delivered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_deliver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'not_cash': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order_status': ('django.db.models.fields.IntegerField', [], {}),
            'paper': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['order']
