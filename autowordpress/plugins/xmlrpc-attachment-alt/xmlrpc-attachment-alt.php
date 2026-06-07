<?php
/*
Plugin Name: XML-RPC Attachment Alt
Description: Añade un método XML-RPC para guardar el texto alternativo de imágenes.
Version: 1.0
Author: Hector
*/

if (!defined('ABSPATH')) {
    exit;
}

add_filter('xmlrpc_methods', function ($methods) {
    $methods['media.set_alt_text'] = 'xmlrpc_set_alt_text';
    return $methods;
});

function xmlrpc_set_alt_text($args) {
    global $wp_xmlrpc_server;

    $wp_xmlrpc_server->escape($args);

    $blog_id       = $args[0];
    $username      = $args[1];
    $password      = $args[2];
    $attachment_id = (int) $args[3];
    $alt_text      = sanitize_text_field($args[4]);

    if (!$wp_xmlrpc_server->login($username, $password)) {
        return $wp_xmlrpc_server->error;
    }

    if (!current_user_can('edit_post', $attachment_id)) {
        return new IXR_Error(401, 'No tienes permisos para editar este adjunto');
    }

    if (get_post_type($attachment_id) !== 'attachment') {
        return new IXR_Error(404, 'El ID indicado no es un adjunto');
    }

    update_post_meta($attachment_id, '_wp_attachment_image_alt', $alt_text);

    return true;
}