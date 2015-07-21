# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Ship.name'
        db.alter_column(u'main_ship', 'name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Location.name'
        db.alter_column(u'main_location', 'name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Member.name'
        db.alter_column(u'main_member', 'name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Member.logoff_ts'
        db.alter_column(u'main_member', 'logoff_ts', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Member.join_ts'
        db.alter_column(u'main_member', 'join_ts', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # Changing field 'Ship.name'
        db.alter_column(u'main_ship', 'name', self.gf('django.db.models.fields.CharField')(default=-1, max_length=100))

        # Changing field 'Location.name'
        db.alter_column(u'main_location', 'name', self.gf('django.db.models.fields.CharField')(default=-1, max_length=100))

        # Changing field 'Member.name'
        db.alter_column(u'main_member', 'name', self.gf('django.db.models.fields.CharField')(default=-1, max_length=100))

        # Changing field 'Member.logoff_ts'
        db.alter_column(u'main_member', 'logoff_ts', self.gf('django.db.models.fields.DateTimeField')(default=-1))

        # Changing field 'Member.join_ts'
        db.alter_column(u'main_member', 'join_ts', self.gf('django.db.models.fields.DateTimeField')(default=-1))

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
            'logoff_ts': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        u'main.ship': {
            'Meta': {'object_name': 'Ship'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        }
    }

    complete_apps = ['main']