# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'ProductBlock'
        db.delete_table('store_productblock')

        # Removing M2M table for field parent on 'ProductBlock'
        db.delete_table('store_productblock_parent')

        # Removing M2M table for field options on 'ProductBlock'
        db.delete_table('store_productblock_options')

        # Adding model 'ProductPart'
        db.create_table('store_productpart', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('store', ['ProductPart'])

        # Adding M2M table for field options on 'ProductPart'
        db.create_table('store_productpart_options', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('productpart', models.ForeignKey(orm['store.productpart'], null=False)),
            ('option', models.ForeignKey(orm['store.option'], null=False))
        ))
        db.create_unique('store_productpart_options', ['productpart_id', 'option_id'])

        # Adding M2M table for field parts on 'Product'
        db.create_table('store_product_parts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm['store.product'], null=False)),
            ('productpart', models.ForeignKey(orm['store.productpart'], null=False))
        ))
        db.create_unique('store_product_parts', ['product_id', 'productpart_id'])


    def backwards(self, orm):
        
        # Adding model 'ProductBlock'
        db.create_table('store_productblock', (
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('store', ['ProductBlock'])

        # Adding M2M table for field parent on 'ProductBlock'
        db.create_table('store_productblock_parent', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('productblock', models.ForeignKey(orm['store.productblock'], null=False)),
            ('product', models.ForeignKey(orm['store.product'], null=False))
        ))
        db.create_unique('store_productblock_parent', ['productblock_id', 'product_id'])

        # Adding M2M table for field options on 'ProductBlock'
        db.create_table('store_productblock_options', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('productblock', models.ForeignKey(orm['store.productblock'], null=False)),
            ('option', models.ForeignKey(orm['store.option'], null=False))
        ))
        db.create_unique('store_productblock_options', ['productblock_id', 'option_id'])

        # Deleting model 'ProductPart'
        db.delete_table('store_productpart')

        # Removing M2M table for field options on 'ProductPart'
        db.delete_table('store_productpart_options')

        # Removing M2M table for field parts on 'Product'
        db.delete_table('store_product_parts')


    models = {
        'store.event': {
            'Meta': {'ordering': "['-priority', 'title']", 'object_name': 'Event'},
            'css': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['store.Product']", 'symmetrical': 'False'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'store.option': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Option'},
            'cost': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'is_cc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['store.Option']", 'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'time': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'store.page': {
            'Meta': {'object_name': 'Page'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['store.Page']", 'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['store.Product']", 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'store.product': {
            'Meta': {'ordering': "['-priority', 'title']", 'object_name': 'Product'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'is_cc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'options': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['store.Option']", 'symmetrical': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['store.Product']", 'null': 'True', 'blank': 'True'}),
            'parts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['store.ProductPart']", 'symmetrical': 'False'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'store.productpart': {
            'Meta': {'object_name': 'ProductPart'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'options': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['store.Option']", 'symmetrical': 'False'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['store']
