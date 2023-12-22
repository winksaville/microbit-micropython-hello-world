# micro:bit MicroPython hello-world

This is Based on https://microbit-micropython.readthedocs.io/en/latest/tutorials/hello.html
and it's just python code edited with a text editor.
I use vim and the use
[`uflash`](https://github.com/ntoll/uflash)
to flash the code onto the micro:bit.

It's a little more than just displaying as it uses `delay` and `loop` parameters of
[`display`](https://microbit-micropython.readthedocs.io/en/latest/display.html) to
control the animation.

# Build

Plug in the microbit into the computers USB port.

```
uflash hello-world.py
```

After 10 seconds or so the program should run
showing displaying the lines:
```
1 HELLO WORLD 1/2 SPEED
2 HELLO WORLD 1/2 SPEED
3 HELLO WORLD 1/2 SPEED
```
And then it will display `Done!` forever.

Also, I've seen
[Error 504](https://support.microbit.org/support/solutions/articles/19000016969-micro-bit-error-codes)
periodically, when running `uflash hello-world.py`. Running agian
typically works.

## License

Licensed under either of

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or http://apache.org/licenses/LICENSE-2.0)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

### Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall
be dual licensed as above, without any additional terms or conditions.

