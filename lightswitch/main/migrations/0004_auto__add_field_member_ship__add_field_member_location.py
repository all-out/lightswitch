# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Member.ship'
        db.add_column(u'main_member', 'ship',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.Ship'], unique=True, null=True),
                      keep_default=False)

        # Adding field 'Member.location'
        db.add_column(u'main_member', 'location',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.Location'], unique=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Member.ship'
        db.delete_column(u'main_member', 'ship_id')

        # Deleting field 'Member.location'
        db.delete_column(u'main_member', 'location_id')


    models = {
        u'main.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        u'main.member': {
            'Meta': {'object_name': 'Member'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'join_ts': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'location': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.Location']", 'unique': 'True', 'null': 'True'}),
            'logoff_ts': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'ship': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.Ship']", 'unique': 'True', 'null': 'True'})
        },
        u'main.ship': {
            'Meta': {'object_name': 'Ship'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        }
    }

    complete_apps = ['main']