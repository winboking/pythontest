# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

from testapp.models import Sale_order,SaleOrderLine,Sale_Type

from django import forms
from django.http import HttpResponseRedirect
import json
from django.db import connection, transaction

import json
import types
from django.db import models
from decimal import *
from django.db.models.base import ModelState
from datetime import datetime,date
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response
from django.db.models import Q


def sale_order_list(req):

    return render_to_response('main.html',{})


def get_saleorder_list(req):

    order = 'desc'
    sort = 'id'
    limit = 20
    offset = 0
    if 'sort' in req.GET:
        sort = req.GET['sort']
        if sort == 'number':
            sort = 'number'
    if 'order' in req.GET:
        order = req.GET['order']
    if 'limit' in req.GET:
        limit = int(req.GET['limit'])
    if 'offset' in req.GET:
        offset = int(req.GET['offset'])
    startjilu = int(offset)
    endjilu = int(offset) + int(limit)

    saleorder_objs = Sale_order.objects.all()


    orderby = ''
    if order == 'desc':
        orderby = '-' + sort
    else:
        orderby = sort
    sqleorder_objs = saleorder_objs.order_by(orderby).values('id', 'name', 'number',)

    zongrowcount = sqleorder_objs.count()

    zongdict = {}
    list1 = []

    for poitem in sqleorder_objs[startjilu:endjilu]:
        dict1 = {}
        dict1['id'] = poitem['id']
        dict1['name'] = poitem['name']
        dict1['number'] = poitem['number']

        list1.append(dict1)
    zongdict['total'] = zongrowcount

    zongdict['rows'] = list1
    return HttpResponse(json.dumps(zongdict), content_type="application/json")


def get_saleorder_list_info(req, order_id):  # 如果上面定义了id  这个地方传递的参数名一定要叫id
    print(order_id)
    order = 'desc'
    sort = 'id'
    limit = 20
    offset = 0
    if 'sort' in req.GET:
        sort = req.GET['sort']
        if sort == 'number':
            sort = 'number'
    if 'order' in req.GET:
        order = req.GET['order']
    if 'limit' in req.GET:
        limit = int(req.GET['limit'])
    if 'offset' in req.GET:
        offset = int(req.GET['offset'])
    startjilu = int(offset)
    endjilu = int(offset) + int(limit)

    saleorderline_objs = SaleOrderLine.objects.filter(order_id=order_id)

    orderby = ''
    if order == 'desc':
        orderby = '-' + sort
    else:
        orderby = sort
        saleorderline_objs = saleorderline_objs.order_by(orderby).values('id', 'price', 'note', )

    zongrowcount = saleorderline_objs.count()

    zongdict = {}
    list1 = []

    for poitem in saleorderline_objs[startjilu:endjilu]:
        dict1 = {}
        dict1['id'] = poitem.id
        dict1['price'] = str(poitem.price)
        dict1['note'] = poitem.note

        list1.append(dict1)
    zongdict['total'] = zongrowcount

    zongdict['rows'] = list1
    return HttpResponse(json.dumps(zongdict), content_type="application/json")


def test2(req):

    return render_to_response('test2.html',{})


def get_treedata(req):

    saletype_objs = Sale_Type.objects.all()

    zongdict = {}
    list1 = []

    for poitem in saletype_objs:
        dict1 = {}
        dict1['type_id'] = poitem.id
        dict1['name'] = poitem.t_name
        dict1['open'] = 'true';
        saleorder_objs = Sale_order.objects.filter(sale_type_id=poitem.id)

        listinfo = []
        for ot in saleorder_objs:
            dinfo = {}
            dinfo['name'] = ot.name
            dinfo['sale_id'] = ot.id
            listinfo.append(dinfo)
        dict1['children'] = listinfo

        list1.append(dict1)

    zongdict['rows'] = list1
    return HttpResponse(json.dumps(zongdict), content_type="application/json")