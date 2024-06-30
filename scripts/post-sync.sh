cd "$(dirname "$0")" || exit 1
cd .. || exit 1
cd backend || exit 1

rm poetry.lock
poetry install
poetry lock
