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

/**
 * Fail-safe regex email extractor for Fluent Forms notifications.
 * Ensures any mixed text (e.g. "client@company.com / +88017...") resolves
 * cleanly to a valid email address so is_email() validation never drops the auto-responder.
 */
add_filter( 'fluentform/email_to', function( $email, $notification = null, $submittedData = null, $form = null ) {
	if ( is_string( $email ) && ! is_email( trim( $email ) ) ) {
		if ( preg_match( '/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/', $email, $matches ) ) {
			return $matches[0];
		}
	}
	return $email;
}, 10, 4 );

