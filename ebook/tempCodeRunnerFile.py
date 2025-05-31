els.PositiveIntegerField(unique=True)  # To maintain chapter sequence

    class Meta:
        ordering = ['order']  # Ensures chapters are retrieved in order

    def __str__(self):
        return f"{self.ebook.name} - {self.title}"