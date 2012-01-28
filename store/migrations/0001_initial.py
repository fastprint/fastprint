# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Page'
        db.create_table('store_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=50, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='\xd0\xbf\xd1\x80\xd0\xb8\xd0\xbd\xd0\xb0\xd0\xb4\xd0\xbb\xd0\xb5\xd0\xb6\xd0\xb8\xd1\x82 \xd0\xba', null=True, to=orm['store.Page'])),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('store', ['Page'])

        # Adding model 'Option'
        db.create_table('store_option', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('cost', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=10, decimal_places=2, blank=True)),
            ('time', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('is_cc', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['store.Option'], null=True, blank=True)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('store', ['Option'])

        # Adding model 'Product'
        db.create_table('store_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('is_cc', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['store.Product'], null=True, blank=True)),
        ))
        db.send_create_signal('store', ['Product'])

        # Adding M2M table for field options on 'Product'
        db.create_table('store_product_options', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm['store.product'], null=False)),
            ('option', models.ForeignKey(orm['store.option'], null=False))
        ))
        db.create_unique('store_product_options', ['product_id', 'option_id'])

        # Adding M2M table for field pages on 'Product'
        db.create_table('store_product_pages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm['store.product'], null=False)),
            ('page', models.ForeignKey(orm['store.page'], null=False))
        ))
        db.create_unique('store_product_pages', ['product_id', 'page_id'])

        # Adding model 'Event'
        db.create_table('store_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('store', ['Event'])

        # Adding M2M table for field products on 'Event'
        db.create_table('store_event_products', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['store.event'], null=False)),
            ('product', models.ForeignKey(orm['store.product'], null=False))
        ))
        db.create_unique('store_event_products', ['event_id', 'product_id'])


    def backwards(self, orm):
        
        # Deleting model 'Page'
        db.delete_table('store_page')

        # Deleting model 'Option'
        db.delete_table('store_option')

        # Deleting model 'Product'
        db.delete_table('store_product')

        # Removing M2M table for field options on 'Product'
        db.delete_table('store_product_options')

        # Removing M2M table for field pages on 'Product'
        db.delete_table('store_product_pages')

        # Deleting model 'Event'
        db.delete_table('store_event')

        # Removing M2M table for field products on 'Event'
        db.delete_table('store_event_products')


    models = {
        'store.event': {
            'Meta': {'ordering': "['-priority', 'title']", 'object_name': 'Event'},
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
            'Meta': {'ordering': "['-priority', 'title']", 'object_name': 'Option'},
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
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'\\xd0\\xbf\\xd1\\x80\\xd0\\xb8\\xd0\\xbd\\xd0\\xb0\\xd0\\xb4\\xd0\\xbb\\xd0\\xb5\\xd0\\xb6\\xd0\\xb8\\xd1\\x82 \\xd0\\xba'", 'null': 'True', 'to': "orm['store.Page']"}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
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
            'pages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['store.Page']", 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['store.Product']", 'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['store']
