

@main.route('/')
def index():
    title = "Welcome to one-minute Pitch!"

    business_pitches = Pitch.get_pitches('business')
    promotion_pitches = Pitch.get_pitches('promotion')
    product_pitches = Pitch.get_pitches('product')
    return render_template('index.html', title=title, business=business_pitches, promotion=promotion_pitches, product=product_pitches)
@main.route('/profile/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    pitches_count = Pitch.count_pitches(uname)
    user_joined = user.date_joined.strftime('%b %d, %Y')
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user=user, pitches=pitches_count, date=user_joined)
