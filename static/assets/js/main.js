(function () {
	if($('.wrapper-menu-hamburger')) {
		$('.wrapper-menu-hamburger').on('click', function() {
			$('.wrapper-menu-hamburger__hamburger-menu').toggleClass('animate');
		})
	}

	if( $('.slider-temp-wrapper__slider-temp') ) {
		$('.slider-temp-wrapper__slider-temp').slick({
			speed: 1000,
			slidesToShow: 1,
			// autoplay: true,
			dots: true,
	
		});
	}

	if($('.category')) {
		$('.category').hover(function() {
			let path = this.querySelector('.category__top-icon svg path')
			if(path) {
				path.setAttribute('fill','')
			}
			}, function() {
			let path = this.querySelector('.category__top-icon svg path')
			if(path) {
				path.setAttribute('fill','url(#icon_gradient)')
			}
		})
	}
})();