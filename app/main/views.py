

@main.route('/')
def index():
    title = "Welcome to one-minute Pitch!"

    business_pitches = Pitch.get_pitches('business')
    promotion_pitches = Pitch.get_pitches('promotion')
    product_pitches = Pitch.get_pitches('product')
    return render_template('index.html', title=title, business=business_pitches, promotion=promotion_pitches, product=product_pitches)
