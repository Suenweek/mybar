import attr
import click


@attr.s(init=False)
class Context(object):

    bar_name = attr.ib()
    app = attr.ib()
    fmt = attr.ib()

    def log(self, msg, *args):
        """Log msg to stderr."""
        if args:
            msg = msg.format(*args)
        click.echo(msg, err=True)


pass_context = click.make_pass_decorator(Context, ensure=True)
