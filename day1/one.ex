defmodule Main do
  def read_file(file_name) do
    File.stream!(file_name) |> Enum.map(&String.trim/1)
  end

  defp handle_line("R" <> rest, lock_num) do
    {turns, _} = Integer.parse(rest)
    new_lock = rem(lock_num + turns, 100)
    zero_count = div(lock_num + turns, 100)
    {new_lock, zero_count}
  end

  defp handle_line("L" <> rest, lock_num) do
    {turns, _} = Integer.parse(rest)
    total_movement = lock_num - turns
    new_lock = rem(total_movement, 100)
    new_lock = if new_lock < 100, do: new_lock + 100, else: new_lock
    zero_count = div(turns - lock_num + 99, 100)
    {new_lock, zero_count}
  end

  def parse_input(input) do
    {lock_pos, zeros} =
      Enum.reduce(input, {50, 0}, fn line, {turns, num_zero} ->
        {lock_pos, zeros} = handle_line(line, turns)
        {lock_pos, num_zero + zeros}
      end)

    {"total: #{lock_pos}", "zero hits: #{zeros}"}
  end
end

lines = Main.read_file("input.txt") |> Main.parse_input()
IO.inspect(lines)
