# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Profile'
        db.create_table('accounts_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('phone', self.gf('django.db.models.fields.IntegerField')(max_length=18)),
            ('is_legal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('accounts', ['Profile'])

        # Adding model 'Legal'
        db.create_table('accounts_legal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Profile'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('inn', self.gf('django.db.models.fields.CharField')(unique=True, max_length=12)),
            ('kpp', self.gf('django.db.models.fields.CharField')(unique=True, max_length=9)),
            ('bik', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('rs', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('ks', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('post', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('accounts', ['Legal'])

        # Adding unique constraint on 'Legal', fields ['title', 'inn']
        db.create_unique('accounts_legal', ['title', 'inn'])

        # Adding model 'Delivery'
        db.create_table('accounts_delivery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Profile'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('accounts', ['Delivery'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Legal', fields ['title', 'inn']
        db.delete_unique('accounts_legal', ['title', 'inn'])

        # Deleting model 'Profile'
        db.delete_table('accounts_profile')

        # Deleting model 'Legal'
        db.delete_table('accounts_legal')

        # Deleting model 'Delivery'
        db.delete_table('accounts_delivery')


    models = {
        'accounts.delivery': {
            'Meta': {'object_name': 'Delivery'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Profile']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'accounts.legal': {
            'Meta': {'unique_together': "(('title', 'inn'),)", 'object_name': 'Legal'},
            'bik': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inn': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'kpp': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '9'}),
            'ks': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'post': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Profile']"}),
            'rs': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'accounts.profile': {
            'Meta': {'object_name': 'Profile'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'is_legal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '18'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['accounts']
