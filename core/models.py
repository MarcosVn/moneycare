# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ContaCorrente(models.Model):
    titulo = models.CharField(max_length=300, verbose_name='Conta Corrente')

    def __unicode__(self):
        return self.titulo


class TipoReceitaDespesa(models.Model):
    titulo = models.CharField(max_length=300, verbose_name='Titulo')

    def __unicode__(self):
        return self.titulo


class ReceitaDespesa(models.Model):
    descricao = models.CharField(max_length=300, verbose_name='Descrição')
    valor = models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Valor')
    data_lancamento = models.DateField(auto_now=True)
    tipo = models.BooleanField(default=True)
    tipo_recebimento_pagamento = models.ForeignKey(TipoReceitaDespesa)
    conta = models.ForeignKey(ContaCorrente)

    def __unicode__(self):
        return self.descricao
