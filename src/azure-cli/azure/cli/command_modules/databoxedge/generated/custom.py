# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=unused-argument

from azure.cli.core.util import sdk_no_wait


def databoxedge_device_list(client,
                            resource_group_name=None,
                            expand=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name,
                                             expand=expand)
    return client.list_by_subscription(expand=expand)


def databoxedge_device_show(client,
                            device_name,
                            resource_group_name):
    return client.get(device_name=device_name,
                      resource_group_name=resource_group_name)


def databoxedge_device_create(client,
                              device_name,
                              resource_group_name,
                              location,
                              tags=None,
                              sku=None,
                              etag=None,
                              data_box_edge_device_status=None,
                              description=None,
                              model_description=None,
                              friendly_name=None,
                              no_wait=False):
    data_box_edge_device = {}
    data_box_edge_device['location'] = location
    data_box_edge_device['tags'] = tags
    data_box_edge_device['sku'] = sku
    data_box_edge_device['etag'] = etag
    data_box_edge_device['data_box_edge_device_status'] = data_box_edge_device_status
    data_box_edge_device['description'] = description
    data_box_edge_device['model_description'] = model_description
    data_box_edge_device['friendly_name'] = friendly_name
    return sdk_no_wait(no_wait,
                       client.create_or_update,
                       device_name=device_name,
                       resource_group_name=resource_group_name,
                       data_box_edge_device=data_box_edge_device)


def databoxedge_device_update(client,
                              device_name,
                              resource_group_name,
                              tags=None):
    return client.update(device_name=device_name,
                         resource_group_name=resource_group_name,
                         tags=tags)


def databoxedge_device_delete(client,
                              device_name,
                              resource_group_name,
                              no_wait=False):
    return sdk_no_wait(no_wait,
                       client.delete,
                       device_name=device_name,
                       resource_group_name=resource_group_name)


def databoxedge_device_download_update(client,
                                       device_name,
                                       resource_group_name,
                                       no_wait=False):
    return sdk_no_wait(no_wait,
                       client.download_updates,
                       device_name=device_name,
                       resource_group_name=resource_group_name)


def databoxedge_device_install_update(client,
                                      device_name,
                                      resource_group_name,
                                      no_wait=False):
    return sdk_no_wait(no_wait,
                       client.install_updates,
                       device_name=device_name,
                       resource_group_name=resource_group_name)


def databoxedge_device_scan_for_update(client,
                                       device_name,
                                       resource_group_name,
                                       no_wait=False):
    return sdk_no_wait(no_wait,
                       client.scan_for_updates,
                       device_name=device_name,
                       resource_group_name=resource_group_name)


def databoxedge_device_show_update_summary(client,
                                           device_name,
                                           resource_group_name):
    return client.get_update_summary(device_name=device_name,
                                     resource_group_name=resource_group_name)


def databoxedge_alert_list(client,
                           device_name,
                           resource_group_name):
    return client.list_by_data_box_edge_device(device_name=device_name,
                                               resource_group_name=resource_group_name)


def databoxedge_alert_show(client,
                           device_name,
                           name,
                           resource_group_name):
    return client.get(device_name=device_name,
                      name=name,
                      resource_group_name=resource_group_name)


def databoxedge_bandwidth_schedule_list(client,
                                        device_name,
                                        resource_group_name):
    return client.list_by_data_box_edge_device(device_name=device_name,
                                               resource_group_name=resource_group_name)


def databoxedge_bandwidth_schedule_show(client,
                                        device_name,
                                        name,
                                        resource_group_name):
    return client.get(device_name=device_name,
                      name=name,
                      resource_group_name=resource_group_name)


def databoxedge_bandwidth_schedule_create(client,
                                          device_name,
                                          name,
                                          resource_group_name,
                                          start,
                                          stop,
                                          rate_in_mbps,
                                          days,
                                          no_wait=False):
    parameters = {}
    parameters['start'] = start
    parameters['stop'] = stop
    parameters['rate_in_mbps'] = rate_in_mbps
    parameters['days'] = days
    return sdk_no_wait(no_wait,
                       client.create_or_update,
                       device_name=device_name,
                       name=name,
                       resource_group_name=resource_group_name,
                       parameters=parameters)


def databoxedge_bandwidth_schedule_update(instance,
                                          device_name,
                                          name,
                                          resource_group_name,
                                          start,
                                          stop,
                                          rate_in_mbps,
                                          days,
                                          no_wait=False):
    if start is not None:
        instance.start = start
    if stop is not None:
        instance.stop = stop
    if rate_in_mbps is not None:
        instance.rate_in_mbps = rate_in_mbps
    if days is not None:
        instance.days = days
    return instance


def databoxedge_bandwidth_schedule_delete(client,
                                          device_name,
                                          name,
                                          resource_group_name,
                                          no_wait=False):
    return sdk_no_wait(no_wait,
                       client.delete,
                       device_name=device_name,
                       name=name,
                       resource_group_name=resource_group_name)


def databoxedge_show_job(client,
                         device_name,
                         name,
                         resource_group_name):
    return client.get(device_name=device_name,
                      name=name,
                      resource_group_name=resource_group_name)


def databoxedge_list_node(client,
                          device_name,
                          resource_group_name):
    return client.list_by_data_box_edge_device(device_name=device_name,
                                               resource_group_name=resource_group_name)


def databoxedge_order_list(client,
                           device_name,
                           resource_group_name):
    return client.list_by_data_box_edge_device(device_name=device_name,
                                               resource_group_name=resource_group_name)


def databoxedge_order_show(client,
                           device_name,
                           resource_group_name):
    return client.get(device_name=device_name,
                      resource_group_name=resource_group_name)


def databoxedge_order_create(client,
                             device_name,
                             resource_group_name,
                             address_line1,
                             postal_code,
                             city,
                             state,
                             country,
                             contact_person,
                             company_name,
                             phone,
                             email_list,
                             status=None,
                             comments=None,
                             address_line2=None,
                             address_line3=None,
                             no_wait=False):
    order = {}
    order['current_status'] = {}
    order['current_status']['status'] = status
    order['current_status']['comments'] = comments
    order['shipping_address'] = {}
    order['shipping_address']['address_line1'] = address_line1
    order['shipping_address']['address_line2'] = address_line2
    order['shipping_address']['address_line3'] = address_line3
    order['shipping_address']['postal_code'] = postal_code
    order['shipping_address']['city'] = city
    order['shipping_address']['state'] = state
    order['shipping_address']['country'] = country
    order['contact_information'] = {}
    order['contact_information']['contact_person'] = contact_person
    order['contact_information']['company_name'] = company_name
    order['contact_information']['phone'] = phone
    order['contact_information']['email_list'] = email_list
    return sdk_no_wait(no_wait,
                       client.create_or_update,
                       device_name=device_name,
                       resource_group_name=resource_group_name,
                       order=order)


def databoxedge_order_update(instance,
                             device_name,
                             resource_group_name,
                             status=None,
                             comments=None,
                             address_line1=None,
                             address_line2=None,
                             address_line3=None,
                             postal_code=None,
                             city=None,
                             state=None,
                             country=None,
                             contact_person=None,
                             company_name=None,
                             phone=None,
                             email_list=None,
                             no_wait=False):
    if status is not None:
        instance.current_status.status = status
    if comments is not None:
        instance.current_status.comments = comments
    if address_line1 is not None:
        instance.shipping_address.address_line1 = address_line1
    if address_line2 is not None:
        instance.shipping_address.address_line2 = address_line2
    if address_line3 is not None:
        instance.shipping_address.address_line3 = address_line3
    if postal_code is not None:
        instance.shipping_address.postal_code = postal_code
    if city is not None:
        instance.shipping_address.city = city
    if state is not None:
        instance.shipping_address.state = state
    if country is not None:
        instance.shipping_address.country = country
    if contact_person is not None:
        instance.contact_information.contact_person = contact_person
    if company_name is not None:
        instance.contact_information.company_name = company_name
    if phone is not None:
        instance.contact_information.phone = phone
    if email_list is not None:
        instance.contact_information.email_list = email_list
    return instance


def databoxedge_order_delete(client,
                             device_name,
                             resource_group_name,
                             no_wait=False):
    return sdk_no_wait(no_wait,
                       client.delete,
                       device_name=device_name,
                       resource_group_name=resource_group_name)


def databoxedge_list_sku(client,
                         filter_=None):
    return client.list(filter=filter_)