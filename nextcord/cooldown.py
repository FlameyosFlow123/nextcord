"""
The MIT License (MIT)
Copyright (c) 2021-present tag-epic
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from nextcord.ext import commands
from nextcord.ext.commands import (
	CooldownMapping as CDM,
	Cooldown as CD,
)
from typing import (
	Callable,
	Optional
)
from .utils import MISSING

def cooldown(rate: Optional[int] = MISSING, per: Optional[float] = MISSING):
	# This
  cooldown = CD(rate=rate, per=per)
  cooldown_mapping = CDM(cooldown)
	# This is to make the decorator itself, and use it like this:
	"""
	import nextcord
	
	client = nextcord.Client(command_prefix="$")
	
	@client.command()
	@cooldown(2, 60.0)
	async def ping(ctx):
		await ctx.send("Pong!")
	"""
  def decorator(func: Callable):
    if isinstance(func, CD):
			# Activates the cooldown.
      func._buckets = cooldown_mapping
     else:
			# Raises the error if it is applied to anything except a command, like a function?
      raise ValueError("Cooldowns must be applied to a command only.")
			
	return decorator
	# This returns the decorator so that this actually works,
	# since this is a decorator function in another function
