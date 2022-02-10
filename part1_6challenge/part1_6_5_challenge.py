# リスト["The", "fox", "jumped", "over", "the", "fence", "."]の文字列を正しい英文になるように連結しよう。単語と単語の間は空白が必要ですが、最後のピリオドの前には空白は不要です。文字列を要素に持つ1つに連結するメソッドがあることを忘れずに！
words = ["The", "fox", "jumped", "over", "the", "fence", "."]
words = " ".join(words)
words = words[0:-2] + "."
print(words)
