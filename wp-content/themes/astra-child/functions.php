<?php
/**
 * Astra Child Theme functions and definitions
 *
 * @package Astra Child - AXELA LTD.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Enqueue scripts and styles.
 */
function axela_child_enqueue_styles() {
	wp_enqueue_style( 'astra-parent-style', get_template_directory_uri() . '/style.css' );
	wp_enqueue_style( 'axela-child-style', get_stylesheet_directory_uri() . '/style.css', array( 'astra-parent-style' ), '1.0.0' );

	// Enqueue Google Fonts (Plus Jakarta Sans & Cormorant Garamond for luxury institutional feel)
	wp_enqueue_style( 'axela-google-fonts', 'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap', array(), null );
}
add_action( 'wp_enqueue_scripts', 'axela_child_enqueue_styles', 15 );
