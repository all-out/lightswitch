# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Members'
        db.delete_table(u'main_members')

        # Deleting model 'Ships'
        db.delete_table(u'main_ships')

        # Adding model 'Ship'
        db.create_table(u'main_ship', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'main', ['Ship'])

        # Adding model 'Member'
        db.create_table(u'main_member', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('logoff_ts', self.gf('django.db.models.fields.DateTimeField')()),
            ('join_ts', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'main', ['Member'])


    def backwards(self, orm):
        # Adding model 'Members'
        db.create_table(u'main_members', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('logoff_ts', self.gf('django.db.models.fields.DateTimeField')()),
            ('join_ts', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'main', ['Members'])

        # Adding model 'Ships'
        db.create_table(u'main_ships', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'main', ['Ships'])

        # Deleting model 'Ship'
        db.delete_table(u'main_ship')

        # Deleting model 'Member'
        db.delete_table(u'main_member')


    models = {
        u'main.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.member': {
            'Meta': {'object_name': 'Member'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'join_ts': ('django.db.models.fields.DateTimeField', [], {}),
            'logoff_ts': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.ship': {
            'Meta': {'object_name': 'Ship'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['main']