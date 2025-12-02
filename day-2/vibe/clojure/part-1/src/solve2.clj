(ns solve2
  (:require [clojure.string :as str]))

;; Idiomatic Clojure solution demonstrating:
;; - Threading macros (->>) for data transformation pipelines
;; - Function composition (comp) for building reusable transformations
;; - transduce for efficient processing of large sequences
;; - juxt for extracting multiple values from maps
;; - partial application for creating specialized functions
;; - Destructuring in function parameters
;; - Lazy sequences with some for early termination
;; - Anonymous functions (#()) for concise transformations

;; Helper function composition utilities
(def parse-long-str
  "Parse string to long - partial application for composition."
  #(Long/parseLong %))

(defn repeating-pattern?
  "Check if a string consists entirely of repeating a prefix pattern.
   Uses some with a lazy sequence for early termination.
   Demonstrates threading macro for data transformation."
  [s]
  (some (fn [prefix-len]
          (->> (subs s 0 prefix-len)
               (java.util.regex.Pattern/quote)
               re-pattern
               (str/split s)
               (every? str/blank?)))
        (range 1 (count s))))

(def invalid-ids-sum
  "Sum all invalid IDs in a range using transduce for efficiency.
   Composes transformations: string conversion, filtering, parsing.
   Returns a function that takes [start end] and returns the sum."
  (fn [[start end]]
    (transduce
     (comp (map str)
           (filter repeating-pattern?)
           (map parse-long-str))
     +
     (range start (inc end)))))

(def parse-range
  "Parse a range string using threading and destructuring.
   Returns a vector [start end] for easy destructuring.
   Uses juxt for extracting map values idiomatically."
  (comp
   (juxt :start :end)
   (partial zipmap [:start :end])
   (partial map parse-long-str)
   #(str/split % #"-")))

(defn -main [& args]
  "Main entry point using a single threading pipeline.
   Reads input, parses ranges, processes each, and sums results.
   Demonstrates idiomatic Clojure data transformation pipeline."
  (->> "input.txt"
       slurp
       str/trim
       (#(str/split % #","))
       (map parse-range)
       (transduce (map invalid-ids-sum) +)
       println))
