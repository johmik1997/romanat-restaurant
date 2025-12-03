<template>
  <section id="testimonials" class="w-full bg-gradient-to-b from-[#f8fafc] to-white py-20">
    <div class="container mx-auto max-w-7xl px-4">
      <!-- Section Header -->
      <div class="text-center mb-16">
        <div class="inline-flex items-center gap-2 bg-[#0f766e] /10 text-[#000000] rounded-full px-4 py-2 mb-6">
          <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/>
          </svg>
          <span class="text-sm font-semibold">Rated 4.9/5 by Our Guests</span>
        </div>
        <h2 class="text-primary text-4xl font-serif font-bold mb-4">
          Guest Experiences
        </h2>
        <p class="max-w-2xl mx-auto text-gray-600 text-lg">
          Discover why our guests keep coming back to experience luxury and tranquility at Serenity Cove.
        </p>
      </div>

      <!-- Testimonials Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-12">
        <TestimonialCard
          v-for="testimonial in testimonials"
          :key="testimonial.id"
          :name="testimonial.name"
          :role="testimonial.role"
          :text="testimonial.text"
          :avatar="testimonial.avatar"
          :rating="testimonial.rating"
          :stay-date="testimonial.stayDate"
          :room-type="testimonial.roomType"
        />
      </div>

      <!-- Stats Section -->
      <div class="bg-white rounded-3xl shadow-xl p-8">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
          <div>
            <div class="text-3xl font-bold text-[#0f766e]  mb-2">4.9/5</div>
            <p class="text-gray-600 text-sm">Guest Rating</p>
          </div>
          <div>
            <div class="text-3xl font-bold text-[#0f766e]  mb-2">98%</div>
            <p class="text-gray-600 text-sm">Would Return</p>
          </div>
          <div>
            <div class="text-3xl font-bold text-[#0f766e]  mb-2">2,500+</div>
            <p class="text-gray-600 text-sm">Happy Guests</p>
          </div>
          <div>
            <div class="text-3xl font-bold text-[#0f766e]  mb-2">4.8/5</div>
            <p class="text-gray-600 text-sm">Service Rating</p>
          </div>
        </div>
      </div>

      <!-- Trust Badges -->
      <div class="mt-12 flex flex-wrap justify-center gap-8 opacity-60">
        <div class="flex items-center gap-2">
          <svg class="w-5 h-5 text-primary" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
          </svg>
          <span class="text-sm text-gray-600">Verified Reviews</span>
        </div>
        <div class="flex items-center gap-2">
          <svg class="w-5 h-5 text-primary" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd"/>
          </svg>
          <span class="text-sm text-gray-600">Secure Booking</span>
        </div>
        <div class="flex items-center gap-2">
          <svg class="w-5 h-5 text-primary" fill="currentColor" viewBox="0 0 20 20">
            <path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"/>
          </svg>
          <span class="text-sm text-gray-600">24/7 Support</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import TestimonialCard from './TestimonialCard.vue'

const testimonials = [
  {
    id: 1,
    name: 'Emma Johnson',
    role: 'Luxury Traveler',
    text: 'From the moment we arrived, the staff made us feel like royalty. Our ocean-view suite was breathtaking, and the private balcony was perfect for morning coffee. The spa treatments were divine!',
    avatar: 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAKsAtwMBIgACEQEDEQH/xAAbAAABBQEBAAAAAAAAAAAAAAADAQIEBQYAB//EADkQAAIBAwIEBAMFBwQDAAAAAAECAwAEERIhBTFBUQYTImEycYEUI0JSoTORscHR4fAVJGJyFkNT/8QAGQEAAwEBAQAAAAAAAAAAAAAAAQMEAAIF/8QAIREAAgMAAgIDAQEAAAAAAAAAAAECAxEhMRJBBCIyURP/2gAMAwEAAhEDEQA/ALrNLmm5pa8s9MfQri7gtVUzyBNXeifh1dMZqm41ZLehHa50BcY0jOAO1dRWglwC4zx+S0WVbWNWeNQfVuW1Z5D2xWGvvEHEbhJ1N0TGX5AAHHtirLivELISPFL505PUjB6Abg+361mrpzPIWMWCeijGaprhhNbME8zlpG1ftO/Wh6sKowOXamkk5wren25UoVnKjG/T3p6EdhlDEAhcZ6A0Nyq7qTjtXTBchEUjHWmeXvk1sMKropJYcyOYoiXBhlDRnGaba+mYAxsxI/EKG64lYMuN8UOzdB2mZjnUSc9f40zWcc8e+N6cxDZOoEBd8ChsxbOMDFEwuBU7hNgt5M0TvoyuzZzg1EEbgZIx296dE5hZTGWBY5+VB9BXZa3fCre3uBHHdqCMavOU757CvQeFXdqlnEsMuURQgLAivLZ55nbLsWfuTSRXEiOpV8MrDBb+dKlW5DY2KPSPZ0OsZGMexpa84sfGF/BMwuYo5IxuUQ4P0NbLg/HLXio+51IwTUUk2IqecHEojOL6LQ0hp3XblSEUs7GV1KRSVjDhQ7m5W2TU46ZGKcDUTiUMckLGVmVEGNQPLNExn73xOVjlKIQ7D7kY2rLzXd3IRK0sutmwxJPKrHiMtnaBHt8uSMamblj6Vn7maSVmYEjUd8GqoRJZyHyOysSX1ZzvjflUczOqZ1Z/KKSPUpL8yBUcktp/407MEt6Fk1yZydOex5UsUgjBDHY8/ekuA0eMsMkZ23FMWFm5iic4OQajuSDjfNcJpMkauVEDCKXBL6MYIFKlq0lyiRMGB61tOktHwu/mDSSQP+NAmWRpPUMajnFW/wBkCvGF1Ifcc6lR8OJhDyD1ClO1IaqWyhgi0BmftgUKc5xqUAjpU5lJn8thssuCPrVhd8IaVNcY3+VF2JdgVTa4KeN7h/UeXTam+a+Acjc8sV2mSGYo2dmxjNNlRotKv8s0zRbWcC+YXJXkBXaVzmQZ3zzpgGlSOeacCAcA1gE6K1j0g6kGoGRYtZAwOlX/AAiOa2u7SWC4y7xMUiBGY9uRz0rMRtJ0KkgEAnrVnwpFnuoRbqH0KwfJ3OeZzj2pU1wNg+T0ThV08kbCV9bgkB8YDVYmsPwSS4tOLm2kiMYeT15f04UZGjudx863HOpJLGVRejTXUppK5OgROBk1R+I5bqSIQwk6TnVgfFj+VXE+fKJA5dKxXizik8Tm2jk0KcatLAkkdP03pkFrOJvEUV0jFVEtwuDyH1waiSKmPQxzjlTTIXYeYSX79zSShxLqBww+GrFwiNvTlBCEu+nJ6jehAHVpCkt2pC+tstk+5p8LLHMHIDZ610cj5ETRpMh1rt/enrCBykBNR1UFXLNlwOXt3owckBGADkZzWMEECtIqK/qbl1rTcG4NpRZMDJ5jFVPALYyz+Y4RogMtvyra8PvOHq4i+0xAj/mKmuk9xFdEYpayH/pZQnSDg9+nyqcnD1dNxj2rRLapIgdXQg8iu4NCNnpfltUspP2WxUfRjbrw2xuzKsuELBjVhLaKI8GtEbbJyTUHiKxQR5lkVO2SN6Pk5YBKMdPPeO2AFydHxFSw9yKpLgAFDqzlAa2PHPIeFZ4ZFbQd8MDtWQuQpRGHQYqyltrkg+RFeXA3RnmcUoRGGFbP0pqPkZO9dIOXTNOJwptl0kmXJ7dRR+H3NxaSRiOby8sGyvX2PWoROX1am92qS4yMkLk55b0GtQU8Z6Iq215HbX4USDUDgc89x77VoVOVzWI8JXcbWsVmzEyByyFh6QP8962MMgIwKhmsZdF6gxrq6krg6K+/nNtZyTKMsvPHSvNOIARTzO2mRQo1aJMksRzJ77itl4r4k9vEkaGPUx2yP37dq89vJPMkA0YVRyA5+9V0x40lul6CsYlVNB0sFBOe9DlycAH1YyzdacsaquthgN+EcvpQy2H77YPvThInwjyifT3xSgL5iA7KaIJiACyqSfalSXrKAo6HTRABhAMuJASvYc6e58+R5TsAMLiiQkBWZyuFzuOdH4XB9ovIYtOMsD8wK5k8QYLWazw/wSJbaN7v1BsNoB2Hzq8m4Tw2VcRwiM45qagXkV8uhbVUIwPiOKDbvxqN9LQwNvzGP61Ktlzpe8jxhY2lrcWLF7S4IB5p0NaKCcyw6m51TWzzOSskeAPxbYqRbXLJqXv+lKm2OgkdxW7mRtNsQD8qpn4TLduJr6bXnn1xUnzfMvcyHI7UDiF7PCmqOCSTV3B2+laHkzmzF2V/FeAWcdtIYNSSAbN71jpIDDmOUY2zk7VqpeI3flqZLU4b8gJxv1zVR4lZorm1fQul12yNqprck8ZLYotbEzwOl6LcDLFl5HpXM33igBfV7cq649UxJ3xVBKJvo57fKiwqQwwpOkZAG5HyoSkHK55VIs5HWVdJAfOlTjlv1oMKLXgV3BDc65lKGNWwQPb9+d63vDn85fOjyycgCMV5/cyNacUaeOOFi76lUEEmt3wCaJ7UeRq8vV+LfB61LavZVU/Rb11dSUgcedcZhmaOWa8mZHY6ipG0h6YPbnWfZmkKeeQc/Ccbirzjl6980Yk9KKutQBVKkTS5kbbA29qtr4RHZywcjs24YEL8BoSLk5Jo8yM2ATkDpmkWMqMkr++mCmDxl/8ArSzaiwVs46Z6VzHQST16UXQGgBGkEdKJhoAVNCga8eurjwlCsl55p/Cuxqp0arfII+I71feDR+1zj0sNqVb+WPoS/wBEjfQ5aPOMn3rmUM+lk3p9hIiDL7+1EuLtA2lE1SnkB1rz9Z6nigE5WOM4ABP4sVADlpcIpPyqVcLIx9a+Yv5VOBQraWe3mZjZmGIfjLhs1uwakQbhnhuQzLjNWaYlRWxv71B4lObmYHQzIB8ajbPapFhK8cao26dzzrpaDhjzDGx0uo0/IVjfG8QVYCvJX0ivQLlYjDqU71gvGjKbZN8kSD+BplT+6F/IilWzLJEx3PfFMY7qMZb2qRECWOMkjfI5UIx+p2LL6mzlTVx5Q1AAQWGMUT0srkuBIeQ70piOfQy47k9KA4bACqDisZEsyq1lHB5a4jcu0nU7d/31pvCV9JbSCJgot1XLgHfJ61l7eYw3IlRSh64J5fStTaWGY0uLaKJ1B3kb1A7DGx980qx8D6uWboHbO2PakoNm7vbp55Gv8TAYB+ldUeFR5hcy4bUnp1Nt7CoUnoDbnOeY5VapZSXCvNIw8oDUQBkg9qhyxa5GZpEwnQ9fpVsWiSSZAOpTpY7nlvXLpOFYbk4pZVUCOQ5JJwafEAIZHK6mB2PamCsByDS2CdPzpzSaoVUqNa/rTAdcmsAn2O9NL4flvWAEaMrhGzpO+KvPCYH2q4QN2Ye/OqeUOGUuR8Odqm+HJfs3FohJ/wCxNJ+dcWLYsbU8mmehWwkwAnWnu0dgdcshMh5n+QpbWQDT0qRdQx3Co+lWeJgy7dRXnLvk9VsBDdRyJqySM42qQbyNVzqI3qTw3iuDoa1GQVJQbbgVbxcTsdCia1YMz6saeW9MUIgcpL0ZC8lgZyyjODnYEUlnOhkKfED07VoOK8SsNbMtrn1BtwB0rN2VvqvWvHGkhdKqOQ96Pijnyf8AAt1K6rgGsL4rlLz28XU5cj9P61ubtlY46d6884zP5/EppSNYX0Lg8h/ma7oj9tFfJn9MI0eYySyhsjGDyoDEo5YJlB0NEhYOdLKScZ2oUmo6t2weQNWnmjiAYPMYb5xtTU9jT4wSjom65yPahDIxgZzWCSY0wVWRjt+Ib4rV+HbsPGllboXBcZb4dPc/SssqMZgUBJUAkgcsVeeEyLvi2WVUBU6lB0knpjG/TvSrFqGVvGby21YB1BlUaTgjnXVGsIpbRFgRAFUfCu+T3NLUelhX8aaOxsX0QpqfmFGA3zrGTSRrE7IrKzbnVuF9+9bPjUCXsYBckptpBxtWV8QSJAiQQlnUYzsOmOtPqeibFhTElhoG++c0aIBbZyepxQUUqDJ+BwcMOmDinO+AuBtjnmqCYYjRqcaMU0sjHKjO+KYGbzcHc04KIm0sMbg78q6ATo2trrAnm+z3Kt6Sw9DDsccqFdyR2soeCVZZuYaPcA96iNgtqyV3JGKCQcknma58Q+R6RwPigvLZTkBxsVPQ1eW1wuSO/vWL4Bb6rOOVThiOlXUUzRuNe2ainFeXB6Ncn4ps0UKHOpT6hyaiNLM5yxGflUe0uIZvibT9akMYTyfFK1lCZFvItTFnKkn2zioTy6AFU7CpV4yx/C2r5VTTyYGc5rpJs4kyNx7iK2tswH7RxpRc8/esUDqiAaIsi82J2zUrjpla78yViTp29qgqzyYRmLKOS9BVtUUo6eddNyk0wsQRjqK4OMZNBC/tAQCeual3H3SRLkBsZFAkGy4IEjHl3pgnBluSAxB/SuTyxjCasc8dKJDq9bBc4GcUqBSSFbGtdRwMY9qBi04XNHFcSKq61lwNP5h2FH8NrCvGkjjJiVGwok2ZsHv+4GgcJWR+K8PCqowwGB1GDkmrfjiE8VigeHy4cBjOi5Yjlkfp/GlSfLQ6K4TNg2c+j0n8wpaRHWSNWQ5DcjS1IVaR54Q8ZXffr1rJ8X4QDJI0aFAAAERdRcnG4ya2Q96hX8BfBQeoDnXcJYzmUdRhuKQx4gWAMNtLgLhRsB/LtVWyE4G/PAHetFxG3u5iV2kcHAC88d6rLvhc1paC4nDIxfGltj9KqhJZySyi94K1AEn9YOcc8de1Nmkdhoxj5VOsbB7y8RIpFDucqHOM11xw+ZJHBjY6M6yFyBg/rTNRxhEghkdSVwMc80zynJAC5ycVKt4ZZcoocluWledGuOEX9tBHNJFIkJIIkP8AT6UQGm8IDXw1cqfS5H61cX1spjBHSqPwhrjtimScPmtTKA0eKgseTZ6Na+iK63hXGRkVIZWX8VJbKNe5qRKnpzXGjF0V8gkY4z+6uktTo3FSYkJfc0WRPTituhwxPie1Z/K0Lj1HNUcNvJFI4cbqM1uOLQa/ffPKoTcKN5LFHEv3sh0JjrmqK7MWEtlOtsynky4BdDnSNJY13kOw1HUABvXoPH/DRgghZX1JEAMN15CqfifB51AMMWkCH1omMk9x3FU9EqjpQ2dpJHMqvG2GdQcnBwaC9u8d08LaUYNjOcjFaqXgc4+zRvDIGAQtIPhcYB2HPOKMOEiyuVuUKSFT6yyaio74pcpNHaimQvCnD/8AemWZJE8lcKrL3FXnH7NLi3jkd1VojnU/y64xU6wtY7aIaCWbABZjnPyo8gSRCjjKnmOhqZybkUqORK/w+rCzYqnoJ9O/P3FdS8N1RvIShjLY+5O+Oe/8KWuH2HCaDXf0xTdVEtIWuZNK7Ac2xyoqLbxGbSWg0hjZxpjDSdwNzUi48OxcUiCXikIDnAO4+vSr6y4cka4VMHueZ+dWSwLpxVkKEuZEtl29GJi8H2NnMZo0dhq1BCdhU7/T4ngaNYlCtzGK1LQgjH8qji20v6BVGITpjOOcKFnDEtlEqMgzqC/FvuBTuN2PleH08xi2qVZQrEnSCCMb56mtsIlEiiQbMPpmmXnDYr1HimUlHUqR7UuUNTO4vGjyzhkfkOVUYBOau0cFN6SfhU3DrowXAByfu3HJx7UqqFYFuRrzpp7yelDM4I8bDzdOcGpTFmTnUaeLD61507zDpwNzQOiTGAqUshBoOsquMVJt7S5vGK28LvjmQNh9aCTb4M2kV0sWsEkcu9aTwrwQwML65TBwRAhG6g8yaseF+Ho7dkkuQJpegHwr7+5q4YHfBwe+Ksppx+UiK6/V4xKziVvqglzjPTUM1WWPDYpSHKjUd8kb/wBq0WkdBj+dcIgDldsjBxVHjrJvLCmezKzgzMSikEe1HFhHKeSvtj1LVk6Kem1NC4pgG2UfEeBvhZLcAH8Qzsf6VSTxTW7aZoyh962+faot5bRXC6ZUDDseVInQpdDoXOPZil9Jy+SehPauqwvuEvEzG2zIv/zJ9Q/rXVK65L0P/wBI/wBIKBncIu7E7VreGWSQQYxlu+KoeAxB7kO2+Nh8616AKxXG46VR8eCUfJiL5vcHouPaigCmsDSBwKpEDyKFJlDkUYYaklXPKsYGQJI8E7jke1Oik1jHJveg5ZDnGaRmzv17isELeW9vdxmO6iDqe45fLtWfu/DLjLWc4fssuxH1/tV8txp/aKaXz7c85Cp+tKnUp/o7hZKH5Mp/4/xEvh4o0H5mkGKnWvhVQP8AdXOT+WJQP1NXxaE7h9R7gUqBGGw1fPalr48UMfyJsgwcE4bbb+QJG7uc/py/SrONPSFCjSOSjYD5ChvrX4FWm6perZpqrihTlJ+w7HA6bcqYd6ZuetKK7w5OxTsCkrt/8NEAwiuIpTXc6xhmKC4zUg0hUH2rBKueLfI2rqlTKK6iDEUfh+LECk82JNaOQgPFL+b4qp+GAC2tcD/MGrKU/wCwU9f71xBYkgzeyZNChlzTNI7UqfBRDXRyDGVoqkdaaaYtYwRkDUMwii0prHRGEQHc/WnKqfiGfnUggdqFIAOlYwgt4jyGn5U8BR0rlpaBhmPem4Hb9aeaXFYwzFLilrqxhK7QO9OrjRADK+9KBXGuFYAuKDPJo07fEcUeoPED99F/2rBGyb11NTeuohP/2Q==',
    rating: 5,
    stayDate: 'June 2024',
    roomType: 'Deluxe King Suite'
  },
  {
    id: 2,
    name: 'Liam Smith',
    role: 'Business Executive',
    text: 'Perfect blend of business and pleasure. The high-speed internet and comfortable workspace made meetings productive, while the infinity pool provided the perfect unwind after work.',
    avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1287&q=80',
    rating: 5,
    stayDate: 'May 2024',
    roomType: 'Executive Suite'
  },
  {
    id: 3,
    name: 'Sophia Lee',
    role: 'Honeymooner',
    text: 'Our honeymoon was absolutely magical thanks to Serenity Cove. The romantic dinner on the beach, couples spa package, and stunning suite made our stay unforgettable. We will definitely return!',
    avatar: 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&auto=format&fit=crop&w=1170&q=80',
    rating: 5,
    stayDate: 'July 2024',
    roomType: 'Presidential Suite'
  }
]
</script>